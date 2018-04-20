'''----------------------------------------------------------------------------------------------
This module makes REST calls
----------------------------------------------------------------------------------------------'''
from json import loads, dumps
import time
import requests
import globals
from mlexceptions import MLProviderFailure, MLInsufficientPermission


def performAlexaTransaction(endpoint, apiToken, post=False, dictBody={}):
    '''----------------------------------------------------------------------------------------------
    Make a REST call to Alexa

    Parameters
    ----------
        endpoint : string
            URL of the REST endpoint
        apiToken : string
            API access token as provided by the original JSON request from Alexa
        post : boolean
            True if transaction is a Post. Otherwise a get (default)
        dictBody : dictionary
            The body of the request (optional)

    Returns
    -------
        dictionary
            The returned response section of the JSON response

    Raises
    ------
        MLProviderFailure
            Something went wrong in the communication
        MLInsufficientPermission
            Skill does not have necessary permissions
    ----------------------------------------------------------------------------------------------'''
    header = {'Authorization': 'Bearer ' + apiToken, 'Accept': 'application/json'}

    # Make the Alexa API call
    try:
        start = time.time()
        if dictBody == {}:
            if post is True:
                jsonResponse = requests.post(endpoint, headers=header)
            else:
                jsonResponse = requests.get(endpoint, headers=header)

            if globals.debug is True:
                print '______________OUR REQUEST____________________'
                print 'Http header: %s' % header
                print 'Endpoint: %s' % endpoint
                if post is True:
                    print 'Post operation'
                else:
                    print 'Get operation'
                print 'jsonBody: n/a'
                print '_____________________________________________'
        else:
            jsonBody = dumps(dictBody)  # Convert payload dictionary to JSON
            if globals.debug is True:
                print '______________OUR REQUEST____________________'
                print 'Http header: %s' % header
                print 'Endpoint: %s' % endpoint
                if post is True:
                    print 'Post operation'
                else:
                    print 'Get operation'
                print 'jsonBody: %s' % str(jsonBody)
                print '_____________________________________________'

            if post is True:
                jsonResponse = requests.post(endpoint, headers=header, data=jsonBody)
            else:
                jsonResponse = requests.get(endpoint, headers=header, data=jsonBody)

        globals.alexaTime = int((time.time() - start) * 1000)
        if globals.debug is True:
            print 'Call took: %s ms' % globals.alexaTime

    except requests.exceptions.TooManyRedirects:
        raise MLProviderFailure('Too many redirects.')
    except requests.exceptions.ConnectionError:
        raise MLProviderFailure('Connection Error')
    except requests.exceptions.Timeout:
        raise MLProviderFailure('Timeout')
    except requests.exceptions.ConnectionError:
        raise MLProviderFailure('Could not connect.')
    except requests.exceptions.RetryError:
        raise MLProviderFailure('Retry failure')
    else:
        # if jsonResponse.status_code == requests.codes.ok:  # If result is good, convert to Dict and return
        if jsonResponse.ok is True:
            dictReturn = loads(jsonResponse.text)
            if globals.debug is True:
                print '______________ALEXA RESPONSE_________________'
                print dictReturn
                print '_____________________________________________'
            return dictReturn
        elif jsonResponse.status_code == 403:  # Forbidden (403) - indicates that the user has not enabled permissions.
            raise MLInsufficientPermission('Alexa device not allowing access to lists')
        else:
            raise MLProviderFailure('Alexa could not process request: ' + str(jsonResponse.status_code) + ' : ' + jsonResponse.text)

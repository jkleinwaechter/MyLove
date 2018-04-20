'''----------------------------------------------------------------------------------------------
This module handles the division of labor for each of the intents. For this skill, most of the
business logic is contained in this module
----------------------------------------------------------------------------------------------'''
import globals
import responses
from cards import buildResponse, buildSpeechletResponse
from lists import findPhrase, addPhraseToList


def handleSessionEndRequest():
    '''----------------------------------------------------------------------------------------------
    Process a 'Cancel' intent

    Parameters
    ----------
        none

    Returns
    -------
        dictionary
            The Alexa JSON Response object
    ----------------------------------------------------------------------------------------------'''
    card_title = globals.alexaListName
    speech = 'Grazie.'
    shouldEndSession = True

    return buildResponse({}, buildSpeechletResponse(card_title, speech, None, shouldEndSession))


def getHelp(request, session):
    '''----------------------------------------------------------------------------------------------
    Produce a help response for the user

    Parameters
    ----------
        request : dictionary
            The 'request' section of the Alexa JSON Request object
        session : dictionary
            The 'session' section of the Alexa JSON Request object
    Returns
    -------
        dictionary
            The Alexa JSON Response object
    ----------------------------------------------------------------------------------------------'''
    session_attributes = {}
    card_title = globals.alexaListName
    reprompt_text = 'Knock Knock'
    shouldEndSession = True

    if globals.debug is True:
        print 'User asked for help.'
    return buildResponse(session_attributes, buildSpeechletResponse(card_title, responses.help(), reprompt_text, shouldEndSession))


def getAffirmation(system):
    '''----------------------------------------------------------------------------------------------
    Get a random affirmation from the list

    Parameters
    ----------
        system : dictionary
            The 'system' section of the Alexa JSON Request object
    Returns
    -------
        dictionary
            The Alexa JSON Response object
    ----------------------------------------------------------------------------------------------'''

    card_title = globals.alexaListName
    reprompt_text = 'Knock knock'
    shouldEndSession = True
    session_attributes = {}

    speech = findPhrase(system)  # Note: By not providing an intent, it is assumed we want a random phrase

    return buildResponse(session_attributes, buildSpeechletResponse(card_title, speech, reprompt_text, shouldEndSession))


def getAffirmationByIndex(system, intent):
    '''----------------------------------------------------------------------------------------------
    Get a specific affirmation from the list

    Parameters
    ----------
        system : dictionary
            The 'system' section of the Alexa JSON Request object
        intent : dictionary
            The 'intent' section of the Alexa JSON Request object
    Returns
    -------
        dictionary
            The Alexa JSON Response object
    ----------------------------------------------------------------------------------------------'''

    session_attributes = {}
    card_title = globals.alexaListName
    reprompt_text = 'Knock knock'
    shouldEndSession = True

    speech = findPhrase(system, intent)

    return buildResponse(session_attributes, buildSpeechletResponse(card_title, speech, reprompt_text, shouldEndSession))


def addAffirmation(system, intent):
    '''----------------------------------------------------------------------------------------------
    Add a spoken item to the list

    Parameters
    ----------
        system : dictionary
            The 'system' section of the Alexa JSON Request object
        intent : dictionary
            The 'intent' section of the Alexa JSON Request object
    Returns
    -------
        dictionary
            The Alexa JSON Response object
    ----------------------------------------------------------------------------------------------'''

    session_attributes = {}
    card_title = globals.alexaListName
    reprompt_text = 'Knock knock'
    shouldEndSession = True

    speech = addPhraseToList(system, intent)

    return buildResponse(session_attributes, buildSpeechletResponse(card_title, speech, reprompt_text, shouldEndSession))

import globals
import responses
from random import randint
from mlexceptions import MLProviderFailure, MLInsufficientPermission, MLCouldNotRetrieveList, MLCouldNotCreateList, MLListNotFound, MLIndexOutOfBounds, MLNoData
from transact import performAlexaTransaction


def findPhrase(system, intent=''):
    '''----------------------------------------------------------------------------------------------
    Find the phrase number indicated

    Parameters
    ----------
        system : dictionary
            The 'system' section of the Alexa JSON Request object
        intent : dictionary
            The 'intent' section of the Alexa JSON Request object

    Returns
    -------
        string
            The phrase to speak or the proper error response
    ----------------------------------------------------------------------------------------------'''
    # Get the list of all available phrases
    try:
        phrases = getPhrasesFromAlexa(system)
    except MLCouldNotRetrieveList:
        return responses.noList()
    except MLCouldNotCreateList:
        return responses.couldNotCreateNewList()
    except MLInsufficientPermission:
        return responses.insufficientPermission()
    except MLListNotFound:  # No initital list, but created one and added primer item
        return responses.createdNewList()

    else:
        if globals.debug is True:
            print phrases

    # Get the item number we will use. (1 based)
    if intent is '':  # no intent json provided, therefore we need to generate a random phrase
        if len(phrases) < 1:
            return responses.emptyList()
        else:
            item = randint(1, len(phrases))
    else:  # a number was sepcified
        try:
            item = getNumberFromSlot(intent)
        except (MLIndexOutOfBounds, ValueError):
            return responses.invalidItemNumber()

    if globals.debug is True:
        print 'Item: %d' % item

    # return the matching phrase
    if 0 < item <= len(phrases):
        return phrases[item - 1]
    else:
        return responses.notEnoughItems(len(phrases))


def getPhrasesFromAlexa(system):
    '''----------------------------------------------------------------------------------------------
    Query Alexa for the list of all of the phrases

    Parameters
    ----------
        system : dictionary
            The 'system' section of the Alexa JSON Request object

    Returns
    -------
        list
            All of the strings in the list

    Raises
    ------
        MLCouldNotRetrieveList
            Alexa not cooperating in retrieveing lists
        MLCouldNotCreateList
            Couldn't create new list in response to not finding one
        MLListNotFound
            There is not a list with the correct name, so we created one
        MLInsufficientPermission
            Need to tell user to enable permissions
    ----------------------------------------------------------------------------------------------'''

    phrases = []

    baseUrl = system['apiEndpoint'] + '/v2/householdlists/'  # the base call for all list functions

    # Get a list of all of the lists available to choose from
    try:
        if globals.debug is True:
            print 'Getting List of Lists'
        listOfLists = performAlexaTransaction(endpoint=baseUrl, apiToken=system['apiAccessToken'])
    except MLInsufficientPermission:
        raise
    except MLProviderFailure:
        raise MLCouldNotRetrieveList(str(baseUrl))

    # Search each one until you find the one we have designated
    found = False  # used to flag whether we found an item or simply exhausted the list
    for list in listOfLists['lists']:
        listName = list['name'].lower()
        listId = list['listId']
        if globals.debug is True:
            print 'List name: ' + listName + '  id:' + listId
        if listName == globals.alexaListName.lower():
            found = True
            if globals.debug is True:
                print 'Found list named ' + globals.alexaListName
            break

    if found is False:   # List not found, so create it and add one item and return List Not found exception
        body = {'name': globals.alexaListName.lower(), 'state': 'active'}
        if globals.debug is True:
            print 'List not found. Attempting to create a new one'
        try:
            newList = performAlexaTransaction(endpoint=baseUrl, apiToken=system['apiAccessToken'], post=True, dictBody=body)
        except MLInsufficientPermission:
            raise
        except MLProviderFailure:
            raise MLCouldNotCreateList(str(baseUrl))
        else:  # we were able to create the list, add a temp item and still need to tell the user we couldn't find his list
            url = baseUrl + newList['listId'] + '/items'
            try:
                if globals.debug is True:
                    print 'New list created. Attempting to add an item'
                body = {'value': responses.defaultPhrase(), 'status': 'active'}
                performAlexaTransaction(endpoint=url, apiToken=system['apiAccessToken'], post=True, dictBody=body)
            except MLInsufficientPermission:
                raise
            except MLProviderFailure:  # Could not create new list
                raise MLCouldNotCreateList(globals.alexaListName)
            # let the caller know that there was not a list, so we created one for the user
            raise MLListNotFound(globals.alexaListName)

    # Next, use the found list id to get the contents of the list we want
    url = baseUrl + listId + '/active'
    if globals.debug is True:
        print 'List found. Retrieving contents.'
    try:
        ourList = performAlexaTransaction(endpoint=url, apiToken=system['apiAccessToken'])
    except MLInsufficientPermission:
        raise
    except MLProviderFailure:
        raise MLCouldNotRetrieveList(url)
    else:  # build a list object with nothing but the returned contents
        for item in ourList['items']:
            phrases.append(item['value'])
        return phrases


def addPhraseToList(system, intent):
    '''----------------------------------------------------------------------------------------------
    Add user stated phrase to the list

    Parameters
    ----------
        system : dictionary
            The 'system' section of the Alexa JSON Request object
        intent : dictionary
            The 'intent' section of the Alexa JSON Request object

    Returns
    -------
        string
            The phrase to speak or the proper error response
    ----------------------------------------------------------------------------------------------'''

    try:
        phrase = getPhraseFromSlot(intent)
    except MLNoData:
        return responses.needAffirmation()
    if globals.debug is True:
        print 'Adding ' + phrase

    baseUrl = system['apiEndpoint'] + '/v2/householdlists/'  # the base call for all list functions

    # Get a list of all of the lists available to choose from
    try:
        if globals.debug is True:
            print 'Getting List of Lists'
        listOfLists = performAlexaTransaction(endpoint=baseUrl, apiToken=system['apiAccessToken'])
    except MLInsufficientPermission:
        return responses.insufficientPermission()
    except MLProviderFailure:
        return responses.noList()

    # Search each one until you find the one we have designated
    found = False  # used to flag whether we found an item or simply exhausted the list
    for list in listOfLists['lists']:
        listName = list['name'].lower()
        listId = list['listId']
        if globals.debug is True:
            print 'List name: ' + listName + '  id:' + listId
        if listName == globals.alexaListName.lower():
            found = True
            if globals.debug is True:
                print 'Found list named ' + globals.alexaListName
            break

    if found is False:   # List not found, so create it and add one item and return List Not found exception
        body = {'name': globals.alexaListName.lower(), 'state': 'active'}
        if globals.debug is True:
            print 'List not found. Attempting to create a new one'
        try:
            newList = performAlexaTransaction(endpoint=baseUrl, apiToken=system['apiAccessToken'], post=True, dictBody=body)
        except MLInsufficientPermission:
            return responses.insufficientPermission()
        except MLProviderFailure:
            return responses.couldNotCreateNewList()
        else:  # we were able to create the list, add a temp item and still need to tell the user we couldn't find his list
            listId = newList['listId']
            if globals.debug is True:
                print 'New list created. Attempting to add an item.'

    url = baseUrl + listId + '/items'
    try:
        body = {'value': phrase, 'status': 'active'}
        performAlexaTransaction(endpoint=url, apiToken=system['apiAccessToken'], post=True, dictBody=body)
    except MLInsufficientPermission:
        return responses.insufficientPermission()
    except MLProviderFailure:
        return responses.couldNotAddItem(phrase)

    return 'I\'ve added, %s' % phrase


def getNumberFromSlot(intent):
    '''----------------------------------------------------------------------------------------------
    Decode the number provided in the slot

    Parameters
    ----------
        intent : dictionary
            The 'intent' section of the Alexa JSON Request object

    Returns
    -------
        int
            An integer of the slot number to use in the array (1 based)
            0 indicates out of bounds

    Raises
    ------
        MLIndexOutofBounds
            Could not detect a value
    ----------------------------------------------------------------------------------------------'''

    if 'INDEX' in intent['slots']:
        slot = intent['slots']['INDEX']
        if 'value' in slot:
            # Future: Need to put in error checking
            value = slot['value']
            return int(value)

    raise MLIndexOutOfBounds(str(slot))  # index to the first character if we can't find one in the slot


def getPhraseFromSlot(intent):
    '''----------------------------------------------------------------------------------------------
    Decode the affirmation provided in the slot

    Parameters
    ----------
        intent : dictionary
            The 'intent' section of the Alexa JSON Request object

    Returns
    -------
        string
            The string that was in the slot
            0 indicates out of bounds

    Raises
    ------
        MLNoData
            Could not detect a value
    ----------------------------------------------------------------------------------------------'''

    value = ''  # default value if not found or empty
    if 'AFFIRMATION' in intent['slots']:
        slot = intent['slots']['AFFIRMATION']
        if 'value' in slot:
            value = slot['value']

    if value == '':
        raise MLNoData
    else:
        return str(value)

'''----------------------------------------------------------------------------------------------
This module contains all of the text handlers that will be used to respopnd to the user.
----------------------------------------------------------------------------------------------'''
import globals


def noList():
    '''----------------------------------------------------------------------------------------------
    Unable to fetch a list

    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''
    if globals.debug is True:
        print 'Unable to fetch a list of lists.'
    return ('I\'m sorry, but there was a problem accessing the list. This is likely a temporary situation. Please try again.')


def insufficientPermission():
    '''----------------------------------------------------------------------------------------------
    Need permissions set

    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''
    if globals.debug is True:
        print 'Insufficient perms'
    return('I need to have permission to access your list.'
           'You can do this by selecting <s> <emphasis level="moderate">Your Skills</emphasis></s> from the Alexa app, choosing, '
           '<s><emphasis level="moderate">' + globals.alexaListName + '</emphasis></s>, and then select <s><emphasis level="moderate">Settings.</emphasis> </s>'
           '<p>Please enable both Read and Write access.</p>')


def createdNewList():
    '''----------------------------------------------------------------------------------------------
    We had to create a new list

    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''
    if globals.debug is True:
        print 'Created new list.'

    # Tell user we created list
    return ('I could not find the list named ' + globals.alexaListName + ', so I created it for you and added an item. '
            'If you would like to learn more about how to add items to your list, just say Alexa, ask ' + globals.alexaListName + ' for help.')


def defaultPhrase():
    '''----------------------------------------------------------------------------------------------
    This is the default message we will add to seed the list if one had to be created

    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''
    return ('I love you.')


def couldNotCreateNewList():
    '''----------------------------------------------------------------------------------------------
    We were unable to create a new list

    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''
    if globals.debug is True:
        print 'Could not create new list'
    return ('I was unable to create a list named ' + globals.alexaListName + '.'
            ' <p>You may want to try and create this list in the Alexa app on your computer or phone.</p>')


def couldNotAddItem(phrase):
    '''----------------------------------------------------------------------------------------------
    We were unable to add an item to the list

    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''

    return ('I was unable to add the phrase ' + phrase + ' to the list named ' + globals.alexaListName + '.'
            ' <p>If this problem persists, you may want to try and create this list in the Alexa app on your computer or phone.</p>')


def emptyList():
    '''----------------------------------------------------------------------------------------------
    The list was empty

    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''

    if globals.debug is True:
        print 'Empty list'
    return('Your list appears to be empty. '
           '<p>You can add items to this list by saying <s> <prosody rate="120%">"Alexa, ask My Love to add I love the way you clean our toilet bowl. "</prosody></s></p>'
           '<p>You can also add and delete items by using your Alexa app on your computer or phone. It is much faster and accurate if you use the Alexa app to populate your list.</p>')


def invalidItemNumber():
    '''----------------------------------------------------------------------------------------------
    Item is not a number

    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''
    if globals.debug is True:
        print 'Invalid item number'
    return ('I\'m sorry, I do not recognize your request. I only understand numbers as an option. Or, just say '
            '<s> <prosody rate="120%">Alexa, ask  ' + globals.alexaListName + '</prosody></s> for a random response.')


def notEnoughItems(count):
    '''----------------------------------------------------------------------------------------------
    List isn't large enough

    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''
    if globals.debug is True:
        print 'not enough items on list - requested #%s' % str(count)
    return ('I\'m sorry, I only have %d items on your list.' % count)


def needAffirmation():
    '''----------------------------------------------------------------------------------------------
    No affirmation provided in request

    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''
    if globals.debug is True:
        print 'No affirmation provided in request'
        return ('I\'m sorry, but I need an affirmation to add to the list.')


def help():
    '''----------------------------------------------------------------------------------------------
    Provide help on using the skill

    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''

    if globals.debug is True:
        print 'Help requested - now with add txt'
        return ('<p>I can randomly read an item from the Alexa list named "' + globals.alexaListName + '". '
                ' Just say "<s> <prosody rate = "120%" >Alexa, ask ' + globals.alexaListName + '."</prosody></s></p> '
                ' <p>You can also ask for a specific number on the list. Just say <s> <prosody rate = "120%">"Alexa, ask ' + globals.alexaListName + ' for number 3."</prosody></s></p> '
                ' <p>You must first have a list named "' + globals.alexaListName + '". You can do this within the Alexa app on your computer or phone. If you do not have a list, I will create one the first time you request a phrase. </p>'
                ' <p>You can add items to this list by saying "<s><prosody rate="120%">Alexa, ask ' + globals.alexaListName + ' to add I Love You ".</prosody></s></p> '
                ' <p>You can also add and delete items by using your Alexa app on your computer or phone.</p> '
                ' <p>I highly recommend using the app for adding items as it is faster and more accurate.</p>')

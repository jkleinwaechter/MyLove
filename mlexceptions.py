'''----------------------------------------------------------------------------------------------
This module contains the exceptions raised within the application
----------------------------------------------------------------------------------------------'''


class Error(Exception):
    '''Base class for exceptions in this module.'''
    pass


class MLNotFound(Error):
    '''use this when we can't find what was requested'''
    def __init__(self, m):
        self.message = "Item NotFound: " + m
        print self.message


class MLProviderFailure(Error):
    '''service provider unable to process'''
    def __init__(self, m):
        self.message = "Provider failure: " + m
        print self.message


class MLInsufficientPermission(Error):
    '''request denied due to insufficient permissions'''
    def __init__(self, m):
        self.message = "Insufficient permission: " + m
        print self.message


class MLCouldNotRetrieveList(Error):
    '''Error getting lists from Alexa'''
    def __init__(self, m):
        self.message = "Could not retrieve list from Alexa: " + m
        print self.message


class MLCouldNotCreateList(Error):
    '''Error in creating new list'''
    def __init__(self, m):
        self.message = "Could not create list from Alexa: " + m
        print self.message


class MLListNotFound(Error):
    '''No list with the recognized name found'''
    def __init__(self, m):
        self.message = "Recognized list name not present: " + m
        print self.message


class MLIndexOutOfBounds(Error):
    '''index into list is not within range'''
    def __init__(self, m):
        self.message = "Index out of bounds: " + m
        print self.message


class MLNoData(Error):
    '''use this when we can't find what was requested'''
    def __init__(self, m):
        self.message = "No Data Found: " + m
        print self.message

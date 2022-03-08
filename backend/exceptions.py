class WikipediaReturnedVoid(Exception):
    """ Raised when Wikipedia found no search results """
    pass


class WikipediaNetworkFail(Exception):
    """ Raised when Wikipedia API fails to connect """
    pass


class WolframReturnedVoid(Exception):
    """ Raised when Wolfram|Alpha found no search results """
    pass


class WolframInvalidClient(Exception):
    """ Raised on an invalid app ID"""
    pass

import tweepy


def login(name):
    lines = []
    with open(name) as f:
        lines = f.readlines()

    apiKey = lines[0].strip("\n")
    apiSecret = lines[1].strip("\n")
    accessToken = lines[2].strip("\n")
    accessTokenSecret = lines[3].strip("\n")
    
    """Create the authentication"""

    authenticate = tweepy.OAuthHandler(apiKey, apiSecret)

    """Set the access token and the access token secret"""

    authenticate.set_access_token(accessToken, accessTokenSecret)

    """Create the API Object"""
    api = tweepy.API(authenticate)
    
    return api





import tweepy

import utils


def get_api(credentials=None):
    """Returns a tweepy api object."""
    if not credentials:
        credentials = utils.read_credentials()

    auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
    auth.set_access_token(credentials["ACCESS_KEY"], credentials["ACCESS_SECRET"])
    api = tweepy.API(auth)

    return api


def tweet(s):
    """Quick n dirty method to post a tweet."""
    api = get_api()
    api.update_status(s)

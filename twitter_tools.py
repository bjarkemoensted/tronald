import tweepy

import config
import utils


def get_api(credentials=None):
    if not credentials:
        credentials = utils.read_credentials()

    auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
    auth.set_access_token(credentials["ACCESS_KEY"], credentials["ACCESS_SECRET"])
    api = tweepy.API(auth)

    return api


def tweet(s):
    api = get_api()
    api.update_status(s)

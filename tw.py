import tweepy
import os

def getKey():
    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_SECRET = os.environ['ACCESS_SECRET']
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)

        
        

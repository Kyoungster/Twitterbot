import tweepy 
import time
import os
from os import environ
import json

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
USER_LIST = json.loads(os.environ['USER_LIST'])
USER_SLIST = str(USER_LIST).replace("'", '"')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

Users = ["Hehe_tv","ceilidhsimone","WHOtheFisJC","spoonie4life","Hehes_Wifey"]

n = 5
while n > 0:
    for userID in Users:
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=userID,  include_rts = False, exclude_replies=True, tweet_mode = 'extended').items(3):                     
            try:
                print(userID)
                print("ID: {}".format(tweet.id))
                print(tweet.created_at)
                print(tweet.full_text)
                tweet.favorite()
                print('Tweet Liked')
                print("\n")
                time.sleep(5)
            except tweepy.TweepError as e:
                print(e.reason)
                print("\n")
            except StopIteration:
                break
    time.sleep(600)        


       

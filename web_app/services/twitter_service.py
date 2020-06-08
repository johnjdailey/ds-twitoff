# web_app/services/twitter_services.py



import os
from pprint import pprint

from dotenv import load_dotenv
import tweepy


load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("AUTH", type(auth))

api = tweepy.API(auth)
print("API CLIENT", type(api))

#def twitter_api_client():
#    return tweepy.API(auth)

if __name__ == "__main__":
    
    screen_name = input("Please input a twitter handle (e.g. johnjdailey): ")

    #
    # how to get information about a given twitter user?
    #

    user = api.get_user(screen_name)
    #> <class 'tweepy.models.User'>
    
    # print(type(user)) 
    # pprint(user._json)
    print(user.id)
    print(user.name)
    print(user.screen_name)
    print(user.followers_count)

    #
    # how to get tweets from a given twitter user?
    #
    
    #tweets = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    tweets = api.user_timeline(screen_name, tweet_mode="extended", count=150)
    #tweet = tweets[0]
    #pprint(dir(tweet))
    #pprint(tweet._json)
    #print(tweet.id)
    #print(tweet.full_text)
    #print(type(tweets)) #> <class 'tweepy.models.ResultSet'>
    
    for tweet in tweets:
        print("-----")
        print(tweet.id, tweet.full_text)
        
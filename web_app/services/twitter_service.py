# web_app/services/twitter_services.py

  
# Access Twitter dev info


# Imports

import os
import tweepy
from pprint import pprint
from dotenv import load_dotenv


# Load in Twitter credentials

load_dotenv()

# Twitter credentials

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


# Set authorization to twitter develop

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("AUTH", type(auth))


# Set api to interact with

api = tweepy.API(auth)
print("API CLIENT", type(api))

#def twitter_api_client():
#    return tweepy.API(auth)


if __name__ == "__main__":
    

    ## Get information about a specific user

    screen_name = input("Please input a twitter handle (e.g. johnjdailey): ")

    
    # How to get information about a given twitter user?
    # Creates object of specific user

    user = api.get_user(screen_name)
    #> <class 'tweepy.models.User'>
    

    #print(type(user)) 
    #pprint(user._json)
    print(user.id)
    print(user.name)
    print(user.screen_name)
    print(user.followers_count)


    ## Getting tweets from the twitter api

    # Returns 20 most recent statuses posted by specific user
    #public_tweets = api.home_timeline()
    #for tweet in public_tweets:
    #    print(tweet.text)

    #tweets = api.user_timeline('s2t2')

    # How to get tweets from a given twitter user?
    # Define how many tweets you want and how much of the tweet to display

    tweets = api.user_timeline(screen_name, tweet_mode="extended", count=150) #exclude_replies=True, include_rts=False)
    tweet = tweets[0]
    #pprint(dir(tweet))
    #pprint(tweet._json)
    print(tweet.id)
    print(tweet.full_text)
    #print(type(tweets)) #> <class 'tweepy.models.ResultSet'>
    
    for tweet in tweets:
        print("-----")
        print(tweet.id, tweet.full_text)
    
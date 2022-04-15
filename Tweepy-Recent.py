#install tweepy
!pip install tweepy
!pip install pandas

#from tweepy import *
import tweepy
import pandas as pd
import csv
import wget
import re
import string
import pandas as pd

# Twitter API key
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET_KEY"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_KEY"

def extract_url(tweet):
    if 'media' in tweet.entities:
        return tweet.entities['media'][0]['media_url_https']
    return ''
	
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
api = tweepy.API(auth)

csvFile = open('sample_data_1.csv', 'a')
csvWriter = csv.writer(csvFile)

first_word = "WORD_A"
second_word = "WORD_B"
new_search = first_word + second_word + " -filter:retweets"
search_words = "WORD_C" 
media_files = set()

# Get image url without space in extract_url def
# Only download latest image (FAIL)
# q={first_word}&{second_word} gets multiple irrelevant images
# q='WORD_A AND WORD_B' get multiple WORD_A or WORD_B images
for tweet in tweepy.Cursor(api.search_tweets,q=search_words,
                           lang="en").items(2000):
    csvWriter.writerow([extract_url(tweet), tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
    print(extract_url(tweet))
    #wget.download(extract_url(tweet))

# Get image url without space in media_files value
# Download images successfully
for tweet in tweepy.Cursor(api.search_tweets,q='WORD_A AND WORD_B',count=100,
                           lang="en",
                           since_id=0).items(2000):
    csvWriter.writerow([extract_url(tweet), tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
    media = tweet.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
for mf in media_files:
    print(media_files)
    wget.download(mf)

print(tweet)

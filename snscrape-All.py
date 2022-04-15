!pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
!pip install pandas
!pip install wget

import os
import pandas as pd
from datetime import date
import snscrape.modules.twitter as sntwitter
import snscrape
import wget
import requests

# Obtain images url from Twitter
media_files = set()
tweets_list = []
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('SEARCH QUERY since:YYYY-MM-DD until:YYYY-MM-DD').get_items()):
    # set maximum number of tweets
    if i>200:
        break
    
    # tweet.media == none if there is no images posted
    if tweet.media:
        for medium in tweet.media:
            # download images for photo's url need to convert
            if isinstance(medium, snscrape.modules.twitter.Photo):
                r = requests.get(medium.fullUrl)
                with open('%s.jpg' % i , 'wb') as fp:
                    fp.write(r.content)
            
            # download images for video' url can use directly
            elif isinstance(medium, snscrape.modules.twitter.Video):
                media_files.add(medium.thumbnailUrl)
				
# Download video images from media_files
for mf in media_files:
    #print(media_files)
    wget.download(mf)
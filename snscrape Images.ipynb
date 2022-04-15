{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8b3ccc2",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "!pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19dace2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install pandas\n",
    "!pip install wget"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3dc2fb77",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "from datetime import date\n",
    "import snscrape.modules.twitter as sntwitter\n",
    "import snscrape\n",
    "import wget\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c6c6baf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Obtain images url from Twitter\n",
    "media_files = set()\n",
    "tweets_list = []\n",
    "for i,tweet in enumerate(sntwitter.TwitterSearchScraper('SEARCH QUERY since:YYYY-MM-DD until:YYYY-MM-DD').get_items()):\n",
    "    # set maximum number of tweets\n",
    "    if i>200:\n",
    "        break\n",
    "    \n",
    "    # tweet.media == none if there is no images posted\n",
    "    if tweet.media:\n",
    "        for medium in tweet.media:\n",
    "            # download images for photo's url need to convert\n",
    "            if isinstance(medium, snscrape.modules.twitter.Photo):\n",
    "                r = requests.get(medium.fullUrl)\n",
    "                with open('%s.jpg' % i , 'wb') as fp:\n",
    "                    fp.write(r.content)\n",
    "            \n",
    "            # download images for video' url can use directly\n",
    "            elif isinstance(medium, snscrape.modules.twitter.Video):\n",
    "                media_files.add(medium.thumbnailUrl)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "40e9630b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Download video images from media_files\n",
    "for mf in media_files:\n",
    "    #print(media_files)\n",
    "    wget.download(mf)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

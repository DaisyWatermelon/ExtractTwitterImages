# Tweet-Image-Extract
## 1. Obtaining data
This repo includes two ways to obtain images from Twitter:
### 1.1 Using snscrape Python library
The snscrape library allows obtaining images from ALL relevant tweets in specific date range without Twitter API key.
install snscrape dev version
```python
!pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
```

### 1.2 Using Tweepy Python library
The latest Tweepy library allows obtain images from RECENT relevant tweets in recent 7 days, cannot set older date, and must use Twitter API key.

## 2. Extract/Download images
This repo includes two ways to download images from the data that obtains in last step:
### 2.1 Wget network downloader
install wget
```python
!pip install wget
```
import wget module
```python
import wget
```
### 2.2 Requests library
import request library
```python
import requests
```
## Links
[snscrape](https://github.com/JustAnotherArchivist/snscrape)

[Tweepy](https://github.com/tweepy/tweepy)

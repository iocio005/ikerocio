import tweepy
from . import models

def twitter_api(tweet, slug):
    twitter = models.TwitterApi.objects.get()
    CONSUMER_KEY = twitter.consumer_key
    CONSUMER_SECRET = twitter.consumer_secret
    ACCESS_KEY = twitter.access_token
    ACCESS_SECRET = twitter.access_token_secret
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    if len(twitter.default_word_long+' en http://ikerocio.com/blog/'+slug) <= 140:
        tweet = '%s en http://ikerocio.com/blog/%s' %(twitter.default_word_long, slug)
    else:
        tweet = '%s: "%s" en http://ikerocio.com/blog/' %(twitter.default_word, tweet)
    try:
        api.update_status(tweet)
    except Exception as e:
        print e

import Config
import text2emotion as te
import tweepy
import json


def searchTweets(query):
    client = Config.get_client()
    auth = tweepy.OAuthHandler(Config.consumer_key, Config.consumer_secret)
    auth.set_access_token(Config.access_token, Config.access_token_secret)
    tapi = tweepy.API(auth)
    tweets = [x._json for x in tweepy.Cursor(tapi.search_tweets, q=query, lang="en", tweet_mode='extended', count = 500).items(500)]
    result = []
    for tweet in tweets:
        result.append(tweet["full_text"])
    return result
 
def emotions(x):  
    emotions = [0,0,0,0,0]
    for a in x:
        a = te.get_emotion(a)
        b = [int(a['Angry']), int(a['Fear']), int(a['Happy']), int(a['Sad']),int(a['Surprise'])]
        for i in range(5):
            emotions[i] += b[i]
    total = sum(x for x in emotions)
    Emotionspct = []
    for x in range(5):
        Emotionspct.append(str(round(emotions[x]/total*100)))
    return Emotionspct

query = input('Enter the word(s) you want analysed: ')
tweets  = searchTweets(query)
emotion = emotions(tweets)
print('In recent tweets mentioning "' + query + '" as sorted by relevance, the sentiments expressed in them are ' + emotion[0] + '% Angry, ' + emotion[1] + '% Fearful, ' + emotion[2] + '% Happy, ' + emotion[3] + '% Sad, and ' + emotion[4] + '% Surprised.')



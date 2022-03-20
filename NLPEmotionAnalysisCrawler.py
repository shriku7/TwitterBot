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
    Angry = 0
    Happy = 0
    Sad = 0
    Surprise = 0
    Fear = 0
    for a in x:
        a = te.get_emotion(a)
        b = [int(a['Angry']), int(a['Fear']), int(a['Happy']), int(a['Sad']),int(a['Surprise'])]
        Angry += b[0]
        Fear += b[1]
        Happy += b[2]
        Sad += b[3]
        Surprise += b[4]
    total = Angry + Fear + Sad + Surprise + Happy
    Emotionspct = [str(round(Angry/total*100)),str(round(Fear/total*100)), str(round(Happy/total*100)), str(round(Sad/total*100)), str(round(Surprise/total*100))]
    return Emotionspct


query = input('Enter the word(s) you want analysed: ')
tweets  = searchTweets(query)
emotion = emotions(tweets)
print('In recent tweets mentioning "' + query + '" as sorted by relevance, the sentiments expressed in them are ' + emotion[0] + '% Angry, ' + emotion[1] + '% Fearful, ' + emotion[2] + '% Happy, ' + emotion[3] + '% Sad, and ' + emotion[4] + '% Surprised.')



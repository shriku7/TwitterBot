import tweepy 
import tkinter

def get_client():
    client = tweepy.Client(bearer_token= 'bearer_token',
                            consumer_key= 'consumer_key',
                            consumer_secret= 'consumer_secret',
                            access_token= 'access_token',
                            access_token_secret= 'access_token_secret')
    return client


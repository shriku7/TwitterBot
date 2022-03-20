import Config

def searchTweets(query):
    client = Config.get_client()
    tweets = client.search_recent_tweets(query=query, max_results = 100)

    tweet_data = tweets.data

    result = []

    if tweet_data is not None and len(tweet_data) > 0 :
        for tweet in tweet_data:
            obj = {}
            obj['id'] = tweet.id
            obj['text'] = tweet.text
            result.append(obj)
    else:
        return []

    return result

tweets  = searchTweets('query')
for tweet in tweets:
    print(tweet)

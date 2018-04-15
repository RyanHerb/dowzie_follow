import twitter

consumer_key = ''
consumer_secret = ''

access_key = ''
access_secret = ''

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_key,
                  access_token_secret=access_secret)

followers = api.GetFollowers()
print(followers)


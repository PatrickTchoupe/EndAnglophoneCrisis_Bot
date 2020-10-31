import tweepy 
from time import sleep

# Import in your Twitter application keys, tokens, and secrets.
# Make sure your credentials.py file lives in the same directory as this .py file. 
from credentials import * 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth)

# Twitter bot setting for liking Tweets 
LIKE = True

print("Twitter bot which retweets, like tweets made with the #EndAnglophoneCrisis") 

# Change the hashtags by your choice

for tweet in tweepy.Cursor(api.search, q = ('#EndAnglophoneCrisis -filter:retweets'),result_type='popular').items(): 
	try: 
		print('\nTweet by: @' + tweet.user.screen_name) 

		tweet.retweet() 
		print('Retweeted the tweet') 

		# Favorite the tweet 
		if LIKE: 
			tweet.favorite() 
			print('Favorited the tweet') 
		
		# Twitter bot sleep time settings in seconds. Use large delays so that you account will not banned
		sleep(60)

	except tweepy.TweepError as e:
		print(e.reason) 

	except StopIteration: 
		break
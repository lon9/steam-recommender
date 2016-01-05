# -*- coding:utf-8 -*-
import twitter
import os
import sys
import utils
from sklearn.externals import joblib
import tweet_analyzer

# Load Twitter information.

consumer_key= os.getenv('ST_CONSUMER_KEY')
consumer_secret = os.getenv('ST_CONSUMER_SECRET')
access_token= os.getenv('ST_ACCESS_TOKEN')
access_token_secret= os.getenv('ST_ACCESS_TOKEN_SECRET')

if not consumer_key or not consumer_secret or not access_token or not access_token_secret:
	print("Twitter information not found.")
	sys.exit(1)


# re_follow follow user defined by screen_name
def re_follow(api, screen_name):
	if not api or not user_id:
		raise ValueError('api or user_id must be set.')

	# Re follow and reply.
	user = api.CreateFriendship(screen_name=screen_name)
	tweet = api.PostUpdate(status='@' + screen_name + ' Thanks to follow me! Please reply to get steam sale recommendation.')


# analyze_twitter analyzes tweets and reply game information for recommendation.
def analyze_twitter(api, status, model_path):
	# Getting tweets.
	tweets = api.GetUserTimeline(screen_name=status.user.screen_name, count=200, include_rts=False, exclude_replies=True)

	analyzer = TweetAnalyzer('model.pkl', 'data.csv') 

	result = analyzer.compare(tweets)


def main():
	api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=access_token_secret)
	for item in api.GetUserStream(withuser='followers'):
		print(item)

if __name__ == '__main__':
	main()

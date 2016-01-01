# -*- coding:utf-8 -*-
import twitter
import os
import sys

consumer_key= os.getenv('ST_CONSUMER_KEY')
consumer_secret = os.getenv('ST_CONSUMER_SECRET')
access_token= os.getenv('ST_ACCESS_TOKEN')
access_token_secret= os.getenv('ST_ACCESS_TOKEN_SECRET')

if not consumer_key or not consumer_secret or not access_token or not access_token_secret:
	print("Twitter information not found.")
	sys.exit(1)


def re_follow(api, screen_name):
	if not api or not user_id:
		return 
	user = api.CreateFriendship(screen_name=screen_name)
	tweet = api.PostUpdate(status='@' + screen_name + ' Thanks to follow me! Please reply to get steam sale recommendation.')

def analyzeTwitter(api, status, model_path):
	if not api or not status or model_path:
		return
	from sklearn.externals import joblib
	km = joblib.load(model_path)
	

def main():
	api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=access_token_secret)
	for item in api.GetUserStream(withuser='followers'):
		print(item)


if __name__ == '__main__':
	main()

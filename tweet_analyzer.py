# -*- coding:utf-8 -*-
import twitter
import os
import utils
from sklearn.externals import joblib
import numpy as np
import scipy as sp


class TweetAnalyzer():

	def __init__(self, dataPath, vectorizedPath, kmeansPath, vectorizerPath):
		# Loading model.
		self.km = joblib.load(kmeansPath)
		if not self.km:
			raise NameError('Model not found named %s' % kmeansPath)


		# Load vactorizer.
		self.vectorizer = joblib.load(vectorizerPath)
		# Load vectorized data.
		self.vectorized = np.load(vectorizedPath)
		# Vectorize existing data.
		self.data = utils.read_data(dataPath)

	def compare(self, tweets):
		target  = ' '.join([self.__extract_english(v) for v in tweets])
		vec = self.vectorizer.transform([target])
		label = self.km.predict(vec)[0]

		similar_indices = (self.km.labels_ == label).nonzero()[0]

		similar = []
		for i in similar_indices:
			dist = sp.linalg.norm((vec - self.vectorized[i]).toarray())
			similar.append((dist, self.data[i]))

		similar = sorted(similar)
		return similar

		
	def __extract_english(self, src):
		if type(src) != unicode:
			raise ValueError('Unicode error')
		return ''.join([c for c in src if ord(c) <=255])

tweets = []
f = open('tweets2.txt', 'r')
for line in f:
	tweets.append(line.decode('utf-8'))

ta = TweetAnalyzer('data.csv', 'vector.npy', 'kmeans.pkl', 'vectorizer.pkl')
similar = ta.compare(tweets)
print(similar)

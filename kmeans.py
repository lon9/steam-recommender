# -*- coding:utf-8 -*-
import csv
import numpy as np
import nltk.stem
from sklearn.externals import joblib
import os
from sklearn.cluster import KMeans
import sys
import utils

class Trainer():
	
	def __init__(self, datapath):
		self.data = utils.read_data(datapath)

	def vectorize(self):
		if not hasattr(self, 'data'):
			print('Data not found')
			sys.exit(1)
		self.vectorizer = utils.StemmedTfidfVectorizer(min_df=10, max_df=0.5, stop_words='english', decode_error='ignore')
		self.vectorized = self.vectorizer.fit_transform(self.data)

	def clustering(self, num_clusters=100):
		if not hasattr(self, 'vectorized'):
			print('Vector not found.')
			sys.exit(1)
		self.km = KMeans(n_clusters=num_clusters, init='random', n_init=1, verbose=1)
		self.km.fit(self.vectorized)

	def storeVector(self, path):
		if not hasattr(self, 'vectorized'):
			print('Vector not found.')
			sys.exit(1)
		# Storing vectorized data.
		np.save(path, self.vectorized)

	def storeKmeans(self, path):
		if not hasattr(self, 'km'):
			print('Model not found.')
			sys.exit(1)
		# Storing clustering model.
		joblib.dump(self.km, path)	

	def storeVectorizer(self, path):
		if not hasattr(self, 'vectorizer'):
			print('Vectorizer not found.')
			sys.exit(1)
		joblib.dump(self.vectorizer, path)

t = Trainer('data.csv')
t.vectorize()
t.clustering()
t.storeKmeans('kmeans.pkl')
t.storeVector('vector.npy')
t.storeVectorizer('vectorizer.pkl')

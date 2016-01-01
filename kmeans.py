# -*- coding:utf-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
import csv
import numpy as np
import nltk.stem
from sklearn.externals import joblib
import os
from sklearn.cluster import KMeans
import sys

class StemmedTfidfVectorizer(TfidfVectorizer):
	
	def build_analyzer(self):
		analyzer = super(TfidfVectorizer, self).build_analyzer()
		english_stemmer = nltk.stem.SnowballStemmer('english')
		return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

class Trainer():
	
	def __init__(self, datapath):
		reader = csv.reader(open(datapath, 'rb'), delimiter=',', quotechar='"')	
		rawdata = []
		for row in reader:
			rawdata.append(row[1])
		self.data = np.array(rawdata)

	def vectorize(self):
		if not hasattr(self, 'data'):
			print('Data not found')
			sys.exit(1)
		english_stemmer = nltk.stem.SnowballStemmer('english')
		vectorizer = StemmedTfidfVectorizer(min_df=10, max_df=0.5, stop_words='english', decode_error='ignore')
		self.vectorized = vectorizer.fit_transform(self.data)

	def clustering(self, num_clusters=50):
		if not hasattr(self, 'vectorized'):
			print('vector not found.')
			sys.exit(1)
		self.km = KMeans(n_clusters=num_clusters, init='random', n_init=1, verbose=1)
		self.km.fit(self.vectorized)

	def storeModel(self, path):
		if not hasattr(self, 'km'):
			print('Model not found.')
			sys.exit(1)
		joblib.dump(self.km, path)	


t = Trainer('data.csv')
t.vectorize()
t.clustering()
t.storeModel('model.pkl')

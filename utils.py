from sklearn.feature_extraction.text import TfidfVectorizer
import nltk.stem

english_stemmer = nltk.stem.SnowballStemmer('english')

class StemmedTfidfVectorizer(TfidfVectorizer):
	
	def build_analyzer(self):
		analyzer = super(TfidfVectorizer, self).build_analyzer()
		return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

def read_data(datapath):
	import csv
	import numpy as np
	reader = csv.reader(open(datapath, 'rb'), delimiter=',', quotechar='"')	
	rawdata = []
	for row in reader:
		rawdata.append(row[1])
	return np.array(rawdata)

def vectorize(data):
	vectorizer = StemmedTfidfVectorizer(min_df=10, max_df=0.5, stop_words='english', decode_error='ignore')
	return vectorizer.fit_transform(data)
	

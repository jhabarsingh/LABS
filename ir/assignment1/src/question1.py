import io
import os
import sys 
import unicodedata
from nltk.corpus import stopwords 
import unicodedata
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer

DEBUG = True

class DataCleaner():
	def __init__(self, filename):
		self.filename = filename
		self.data = None
	
	def getText(self):
		return self.data
	
	def assignData(self):
		newData = ""
		with open(self.filename, "rb") as rfile:
			lines = rfile.readlines()
			for i in lines:
				newData += str(i)
		newData.replace("\\n", " ")
		self.data = newData
		return newData
		
	def removeAccent(self):
		nfkd_form = unicodedata.normalize('NFKD', self.data)
		return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])		
		
		
	def removestopWord(self):
		stop_words = set(stopwords.words('english')) 
		words = self.data.split()		
		newData = ""
		for r in words: 
			if not r in stop_words: 
				newData += r		
		return newData
	

	def stemming(self):
		ps = PorterStemmer()
		words = self.data.split()
		newData = ""
		for w in words:
    			newData += ps.stem(w)
		return newData
	
		
if __name__ == "__main__":
	filename = sys.argv[1]
	datacleaner = DataCleaner(filename)
	datacleaner.assignData()
	if DEBUG:
		print(datacleaner.getText())
		
	print(datacleaner.removeAccent())
	print(datacleaner.stemming())
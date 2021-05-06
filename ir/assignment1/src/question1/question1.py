import io
import re
import os
import sys 
import string
import unicodedata
import nltk
from nltk.corpus import stopwords 
import unicodedata
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
lemmatizer = WordNetLemmatizer()

nltk.download('wordnet')
nltk.download('stopwords')

DEBUG = False

class DataCleaner():
	def __init__(self, filename):
		self.filename = filename
		self.data = None
	
	def getText(self):
		return self.data
	
	def removeSpaces(self, data):
		return re.sub(' +', ' ', data)
	

	def removeNumPun(self, data):
		data = re.sub(r'\d+', '', data)
		translator = str.maketrans('', '', string.punctuation)
		return data.translate(translator)
	
	def replaceNewline(self, data):
		return data.replace('\\n', '\n')

	
	def replaceReturnCarrige(self, data):
		return data.replace('\\r', '')

	def assignData(self):
		newData = ""
		with open(self.filename, "rb") as rfile:
			newData = rfile.read()
			self.data = str(newData)[2:-1]
			self.data = self.removeSpaces(self.data)
			self.data = self.replaceNewline(self.data)
			self.data = self.replaceReturnCarrige(self.data)

		return newData
		
	def removeAccent(self):
		nfkd_form = unicodedata.normalize('NFKD', self.data)
		return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])		
		
		
	def removestopWord(self):
		stop_words = set(stopwords.words('english')) 
		words = self.data.split()		
		newData = ""
		newData = [word for word in words if word not in stopwords.words('english')]		
		return " ".join(newData)
	

	def stemming(self):
		ps = PorterStemmer()
		words = self.data.split()
		newData = ""
		for w in words:
    			newData += ps.stem(w) + " "
		return newData

	def lemmatize(self):
		lm = WordNetLemmatizer()
		words = self.data.split()
		newData = ""
		for w in words:
			newData += lm.lemmatize(w) + " "
		return newData

		
	def removeSingleLetter(self):
		data = self.data.split()
		temp = ""
		for word in data:
			if len(word) > 1:
				temp += word + " "
		return temp

	
	def cleanData(self):
		self.data = self.removeAccent()
		self.data = self.removestopWord()
		self.data = self.removeNumPun(self.data)
		self.data = self.stemming()
		self.data = self.lemmatize()
		self.data = self.removestopWord()
		self.data = self.removeSingleLetter()
		return self.data

	def createFile(self, data):
		filename =self.filename.split('.')[0] + "_output." + self.filename.split('.')[1]
		with open(filename, "w+") as wfile:
			wfile.write(data)
		os.system(f'mv {filename} outputs')	
		return True

	def countWords(self, input, output):
		return len(input.split()) - len(output.split())	
		

if __name__ == "__main__":
	filename = sys.argv[1]
	datacleaner = DataCleaner(filename)
	datacleaner.assignData()
	input = datacleaner.getText()
	if DEBUG:
		print(datacleaner.getText())
	
	
	changedData = datacleaner.cleanData()

	datacleaner.createFile(changedData)
	print(f"File words difference {datacleaner.countWords(input, changedData)}")

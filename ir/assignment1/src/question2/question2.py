import sys
import os
import json

LEN = 15
LEFT = 38
class InvertedIndex():
	def __init__(self, filename):
		self.filename = filename
		self.data = None
		self.invertedindex = None
		self.query = None	
	
	def createInvertedIndex(self):
		tokenized_data = self.data.split()
		
		inverted = {}
		for index, word in enumerate(tokenized_data):
			locations = inverted.setdefault(word, [])
			locations.append(index)
		self.invertedindex = inverted
		
	def searchInvertedIndex(self):
		text = self.query
		query = text.split()
		print("-" * 101)
		print("|", end="")
		print(" " * LEFT, end="")
		print("INVETED INDEX SEARCHING", end="")
		print(" " * LEFT, end="")
		print("|")
		print("-" * 101)
		
		for word in query:
			for keys in self.invertedindex.keys():
				if keys == word:
					for i in range(LEN):
						if i < len(keys):
							print(keys[i], end="")
						else:
							print(" ", end="")
					print("|", end="")
					for i in range(10):
						print(" ", end="")
					print(self.invertedindex[keys])

	def initializeText(self):
		text = ""
		with open(self.filename, "r") as rfile:
			text += rfile.read()
		self.data = text
	
	def initializeQuery(self, filename):
		text = ""
		with open(filename, "r") as rfile:
			text += rfile.read()
		self.query = text
	
	def printInvertedIndex(self):
		data = self.invertedindex
		data = str(json.dumps(data, indent=3))
		
		with open("inverted.txt", "w") as wfile:
			wfile.write(data)

if __name__ == "__main__":
	
	filename = sys.argv[1]
	inverted_index = InvertedIndex(filename)
	inverted_index.initializeText()
	inverted_index.createInvertedIndex()
	
	filename = sys.argv[2]

	inverted_index.initializeQuery(filename)

	inverted_index.searchInvertedIndex()

	inverted_index.printInvertedIndex()

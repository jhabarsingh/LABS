with open("stopwords.js", "r+") as file:
	words = file.readlines()
	word = []
	for i in words:
		word.append(i.replace("\n", ""))
	print(word)

def revword(word):
	word=word.lower()
	x=len(word)-1
	drow=word[x]
	x=x-1
	while x>=0:
		drow=drow+word[x]
		x=x-1
	return drow

def countword():
	try: 
		file=open('./text.txt', 'r')
	except: 
		print('file can not be open')
		quite()
	counter=0
	word=file[0].strip()
	for line in file:
		words_line=line.split()
		for words in words_line:
			name=revword(words)
			if name==word:
				counter=counter+1
		
	if word!=revword(word):
		counter=counter+1
	return counter	

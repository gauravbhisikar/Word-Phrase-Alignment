with open("parse",'r') as f:
	parse = f.readlines()

sentence = ""
for i in range(len(parse)):
	parse[i] = parse[i].replace('\n','').replace('  ',"") + " "

for i in parse:
	sentence += i

print(sentence)
print("------------------------------------------\n\n")


index = []
tag   = []
level = []
word  = []
table = []


tempIndex = 0
tempTag = ""
tempLevel = 0
tempGapIndx = 0
tempWord = ""
for i in range(len(sentence)):
	if(sentence[i] == "("):
		level.append(tempLevel)
		tempLevel+=1
		index.append(tempIndex)
		tempIndex+=1
		for j in range(i+1,len(sentence)):
			if(sentence[j] == " "):
				break
			else:
				tempTag+= sentence[j]
		tag.append(tempTag)
		tempTag = ""
		for j in range(i+1,len(sentence)):
			if (sentence[j] != " " and sentence[j] == "("):
				word.append("-")
				break
			if (sentence[j] == ")"):
					for x in range(i+1,len(sentence)):
						if (sentence[x] == " "):
							tempGapIndx = x
							break
					for x in range(tempGapIndx,len(sentence)):
						if (sentence[x] == ")"):
							tempGapIndx = 0
							break
						else:
							tempWord += sentence[x]	
					word.append(tempWord)
					tempWord = ""
					break
								
	if(sentence[i] == ")"):
		tempLevel -= 1				

	
tempTable = []

for i in range(len(index)):
	tempTable.append(index[i])
	tempTable.append(tag[i])
	tempTable.append(level[i])
	tempTable.append(word[i])
	table.append(tempTable)
	tempTable = []

for i in table:
	print(i)	
	



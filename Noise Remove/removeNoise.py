# USAGE 
# python removeNoise.py fileName


import sys

file = sys.argv[1]


def combChapterInt(sentence):
	intgers = ['1','2','3','4','5','6','7','8','9','0']
	temp = []
	flag = 0
	remove = ""
	for i in range(len(sentence)):
		if (sentence[i] == 'Chapter') and (sentence[i+1] in intgers):
			temp.append(f"{sentence[i]} " + f"{sentence[i+1]}")
			flag = 1
			remove = sentence[i+1]
		if (sentence[i]=='CHAPTER') and (sentence[i+1][0] in intgers):
			temp.append(f"{sentence[i]} " + f"{sentence[i+1]}")
			flag = 1
			remove = sentence[i+1]
		if (sentence[i] == 'Figure' and (sentence[i+1][0]in intgers)):
			temp.append(f"{sentence[i]} " + f"{sentence[i+1]}")
			flag = 1
			remove = sentence[i+1]
		else:
			if sentence[i] !="CHAPTER":
				if sentence[i] !="Chapter":
					temp.append(sentence[i])	

	return temp,remove




def removeNoise(sentence,remove):
	noise = [f"Chapter {remove}","Introduction","INTRODUCTION","CHAPTER",f"CHAPTER {remove}",f"Figure {remove}"]
	for word in sentence:
		if word in noise:
			sentence.remove(word)
	if remove!="":
		sentence.remove(remove)
	return sentence		

temp = []
count = 0


with open(file,"r") as read:
	sentence = read.readlines()


for i in range(len(sentence)):
	sentence[i] = sentence[i].split()


for i in range(len(sentence)):
	sent,remove = combChapterInt(sentence[i])
	sentenceToWrite = removeNoise(sent,remove)
	temp.append(sentenceToWrite)
	count +=1

final = ""
for i in range(count):
	for j in range(len(temp[i])):
		final += temp[i][j] + " "	
	final += '\n'

with open(f"{sys.argv[1]}_noiseRemoved.txt","w") as write:
	write.writelines(final)

	






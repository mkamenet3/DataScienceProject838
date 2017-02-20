import os
import sys
import random


# max number of words to get before and after the title
MAXWORDS = 3
# max number of negtive examples from each document
MAXNEG = 10
# max number of words in negtive examples
MAXNEGWORDS = 3

# output list of examples for feature generation
# use this as the input of feature generation
# format: (title, wordsbefore, wordsafter, class)
outlist = []

ouputfile = open("examples.txt",'w')

pos_num = 0
neg_num = 0
badfile_num = 0
file_num = 0

# path to the html folder
newpath = './tagged/'
files = os.listdir(newpath)
for file in files:
	with open(newpath+file) as f:
		#print(file)
		ouputfile.write(file+'\n')

		file_num += 1
		# wrap all lines without new line charactar
		lines=""
		for line in f:
			lines += line.strip()
		words = lines.split(" ")

		title = ""
		within = False
		wordsprocessed = []
		badfile = False
		for i in range(len(words)):
			tmplist = []
			word = words[i]
			if word == '': continue
			#print(word)
			pos1 = word.find("<myy>")
			pos2 = word.find("</myy>")
			# if no tag found
			if pos1 == -1 and pos2 == -1:
				wordsprocessed.append((word,within))
			# if both are found
			if pos1 >= 0 and pos2 >= 0:
				tmplist = word.split("<myy>")
				if len(tmplist)>2 or pos2 < pos1: 
					badfile = True
					break
				if tmplist[0]!='':
					wordsprocessed.append((tmplist[0],within))
				within = True
				tmplist = tmplist[1].split("</myy>")
				wordsprocessed.append((tmplist[0],within))
				within = False
				if tmplist[1]!='':
					wordsprocessed.append((tmplist[1],within))
				continue
			# if only start tag
			if pos1 >= 0:
				tmplist = word.split("<myy>")
				if len(tmplist)>2: 
					badfile = True
					break
				if tmplist[0]!='':
					wordsprocessed.append((tmplist[0],within))
				within = True
				wordsprocessed.append((tmplist[1],within))
				continue
			# if only end tag
			if pos2 >= 0:
				tmplist = word.split("</myy>")
				if len(tmplist)>2: 
					badfile = True
					break
				wordsprocessed.append((tmplist[0],within))
				within = False
				if tmplist[1]!='':
					wordsprocessed.append((tmplist[1],within))

		if badfile is True: 
			badfile_num += 1
			continue

		# get positive examples from the processed words
		wordsbefore = []
		wordsafter = []
		title = ""
		for i in range(len(wordsprocessed)):
			item = wordsprocessed[i]
			if item[1] is True:
				# if it is the first word
				if i == 0:
					title += item[0]
					while len(wordsbefore) < MAXWORDS:
						wordsbefore.append(None)
				# if word before is also title
				elif wordsprocessed[i-1][1]:
					title += " " + item[0]
				else:
					title += item[0]
					# get words before the title
					for j in range(i-1,i-1-MAXWORDS,-1):
						if j >= 0:
							wordsbefore.append(wordsprocessed[j][0])
						else:
							# add empty element
							while len(wordsbefore) < MAXWORDS:
								wordsbefore.append(None)
							break
			else:
				# if the word before this is title
				if i != 0 and wordsprocessed[i-1][1]:
					# get words after the title
					for j in range(i,i+MAXWORDS):
						if j < len(wordsprocessed):
							wordsafter.append(wordsprocessed[j][0])
						else:
							# add empty element
							while len(wordsafter) < MAXWORDS:
								wordsafter.append(None)
							break
					# add title and words before and after to output list
					featuretuple = (title, wordsbefore, wordsafter, True)
					#print(featuretuple)
					outlist.append(featuretuple)

					# generate output string
					# this part can be skipped if only want features
					outstr = title + ", ["
					for w in wordsbefore:
						if w is None:
							outstr += 'None '
						else:
							outstr += w + ' '
					outstr += '], ['
					for w in wordsafter:
						if w is None:
							outstr += 'None '
						else:
							outstr += w + ' '
					outstr += '], T\n'
					ouputfile.write(outstr)

					pos_num += 1

					title = ""
					wordsbefore = []
					wordsafter = []

		# get negtive examples
		wordsbefore = []
		wordsafter = []
		title = ""
		count = 0
		poslist = []
		# skip the document if there are not enough words in it
		if len(wordsprocessed) < 100:
			continue
		while count < MAXNEG:
			pos = random.randint(MAXWORDS+1, len(wordsprocessed)-MAXWORDS-MAXNEGWORDS)
			title_len = random.randint(1,MAXNEGWORDS)
			# get neg title
			alltrue = True
			for i in range(title_len):
				if wordsprocessed[pos+i][1] is False:
					alltrue = False
				title += wordsprocessed[pos+i][0] + " "
			# if all words are in title
			if alltrue is True:
				title = ""
				continue
			title = title.strip()
			# get words before and after
			for i in range(0,MAXWORDS):
				wordsbefore.append(wordsprocessed[pos-i-1][0])
				wordsafter.append(wordsprocessed[pos+title_len+i][0])
			featuretuple = (title, wordsbefore, wordsafter, False)
			#print(featuretuple)
			outlist.append(featuretuple)

			# generate output string
			# this part can be skipped if only want features
			outstr = title + ", ["
			for w in wordsbefore:
				if w is None:
					outstr += 'None '
				else:
					outstr += w + ' '
			outstr += '], ['
			for w in wordsafter:
				if w is None:
					outstr += 'None '
				else:
					outstr += w + ' '
			outstr += '], F\n'
			ouputfile.write(outstr)


			neg_num += 1
			count += 1
			title=""
			wordsbefore = []
			wordsafter = []

ouputfile.close()
print("number of pos examples:", pos_num)
print("number of neg examples:", neg_num)
print("number of bad files:", badfile_num)
print(file_num)

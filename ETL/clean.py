import csv
inputfile = open('movie_metadata.csv')
outputfile = open('movie_metadata_clean.csv','w')
reader = csv.DictReader(inputfile,skipinitialspace=True)
header = reader.fieldnames
writer = csv.DictWriter(outputfile, fieldnames=header)
writer.writeheader()

for row in reader:
	for key, value in row.items():
		row[key] = row[key].lower()
		row[key] = row[key].strip()

		if row[key] == '':
			row[key] = '.'

		if key == 'genres' or key == 'plot_keywords':
			keywords = row[key].split('|')
			newstr = keywords[0]
			for i in range(1, len(keywords)):
				newstr += '|' + keywords[i].strip()


	writer.writerow(row)


inputfile.close()
outputfile.close()

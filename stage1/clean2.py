import csv
inputfile = open('film.csv',encoding='mac_roman')
outputfile = open('film_clean.csv','w',encoding='utf-8')
reader = csv.DictReader(inputfile,delimiter=';',skipinitialspace=True)
header = reader.fieldnames

# clean header
for i in range(len(header)):
        header[i] = header[i].lower().strip()


writer = csv.DictWriter(outputfile,delimiter=',',fieldnames=header)
writer.writeheader()

line_no = 0
for row in reader:
        line_no += 1
        if line_no == 1:
                continue
        for key, value in row.items():
                row[key] = row[key].lower()
                row[key] = row[key].strip()
                row[key].replace(',', '')
                if row[key] == '':
                        row[key] = '.'
                if key == 'actor' or key == 'actress' or key == 'director':
                        row[key] = row[key].replace(',','')
        writer.writerow(row)


inputfile.close()
outputfile.close()

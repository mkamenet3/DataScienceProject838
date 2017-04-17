import sys
import csv
import pandas as pd
import numpy as np

# merge genres
def MergeGenres(g1,g2):
	g1 = g1.lower().strip().split('|')
	g2 = g2.lower().strip().split('|')
	gm = g1 + g2
	gm = list(set(gm))
	gmstr = gm[0]
	for i in range(1,len(gm)):
		gmstr += '|' + gm[i]
	return gmstr

# calculate Jaccard similarity between two strngs
def jaccard_similarity(s1, s1):
	t1 = s1.lower().string().split(' ')
	t2 = s2.lower().string().split(' ')
    intersection = set(t1).intersection(set(t2))
    union = set(t1).union(set(t2))
    return 1.0*len(intersection)/len(union)


mlid = []
mrid = []
m1data = {}
m2data = {}

# input data
m1file = open('movie1_stage3.csv','r',encoding='mac_roman')
m2file = open('movie2_stage3.csv','r',encoding='mac_roman')
matchfile = open('pospredictions.csv','r',encoding='mac_roman')
m1reader = csv.DictReader(m1file)
m2reader = csv.DictReader(m2file)
# m1 = pd.read_csv('movie1_stage3.csv',index,encoding='mac_roman')
# m2 = pd.read_csv('movie2_stage3.csv',encoding='mac_roman')
matchreader = csv.DictReader(matchfile)

# output file
outputfile = open('movie_merged.csv','w',encoding='mac_roman')
fieldnames = ['lid','rid','title','year','genres']
outputwriter = csv.DictWriter(outputfile,fieldnames = fieldnames)
outputwriter.writeheader()

# initialize match id lists
for row in matchreader:
	lid = int(row['ltable_id'])
	rid = int(row['rtable_movieId'])
	if lid not in mlid and rid not in mrid:
		mlid.append(lid)
		mrid.append(rid)

print(len(mlid))

# load input tables 
for row in m1reader:
	m1data[int(row['id'])] = row
for row in m2reader:
	m2data[int(row['movieId'])] = row

# merge table
outdict = {}
# step1: merge movies in m1
for lid, movie in m1data.items():
	outdict['lid'] = str(lid)
	if lid in mlid:
		i = mlid.index(lid)
		rid = mrid[i]
		outdict['rid'] = str(rid)
		outdict['title'] = m2data[rid]['title']
		outdict['year'] = m2data[rid]['year']
		# merge genres
		g1 = m1data[lid]['genres']
		g2 = m2data[rid]['genres']
		outdict['genres'] = MergeGenres(g1,g2)
		# remove movie from m2
		m2data.pop(rid)
	else:
		outdict['rid'] = ''
		outdict['title'] = movie['movie_title']
		outdict['year'] = movie['title_year']
		outdict['genres'] = movie['genres']
	outputwriter.writerow(outdict)
	outdict = {}

# step 2: add remaining movies in m2
for rid, movie in m2data.items():
	outdict['lid'] = ''
	outdict['rid'] = str(rid)
	outdict['title'] = movie['title']
	outdict['year'] = movie['year']
	outdict['genres'] = movie['genres']
	outputwriter.writerow(outdict)
	outdict = {}



outputfile.close()
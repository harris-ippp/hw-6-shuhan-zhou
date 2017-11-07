#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import glob
import re 
import os

path = '/Users/shuhan_zhou/Documents/Github/hw-6-shuhan-zhou'

allFiles = glob.glob(path + "/president_general_*")


frame = pd.DataFrame()
list_ = []

for file_ in allFiles:

	header = pd.read_csv(file_, nrows = 1).dropna(axis = 1)
	d = header.iloc[0].to_dict()

	df = pd.read_csv(file_, index_col = 0,
	               thousands = ",", skiprows = [1])

	df.rename(inplace = True, columns = d) # rename to democrat/republican
	df.dropna(inplace = True, axis = 1)    # drop empty columns
	df = df[['Democratic','Republican', 'Total Votes Cast']]

	
	df["Year"] = os.path.basename(file_).split('_')[2]


	list_.append(df)

frame = pd.concat(list_)
frame['Year'] = frame['Year'].apply(lambda x: x.split('.')[0])


frame['Republican Vote Share'] = frame['Republican']/frame['Total Votes Cast']

frame['county'] = frame.index


acco = frame[frame['county'] == 'Accomack County']
acco_ax = plt.plot(acco['Year'], acco['Republican Vote Share'])
plt.xlabel("Year")
plt.ylabel("Republican Vote Share")
plt.savefig('accomack_county.pdf')

alber = frame[frame['county'] == 'Albermarle County']
alber_ax = plt.plot(acco['Year'], acco['Republican Vote Share'])
plt.xlabel("Year")
plt.ylabel("Republican Vote Share")
plt.savefig('albermarle_county.pdf')


al = frame[frame['county'] == 'Alexandria County']
al_ax = plt.plot(acco['Year'], acco['Republican Vote Share'])
plt.xlabel("Year")
plt.ylabel("Republican Vote Share")
plt.savefig('alexandria_county.pdf')


alle = frame[frame['county'] == 'Alleghany County']
alle_ax = plt.plot(acco['Year'], acco['Republican Vote Share'])
plt.xlabel("Year")
plt.ylabel("Republican Vote Share")
plt.savefig('alleghany_county.pdf')















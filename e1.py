#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
import requests 
import re

addr = 	"http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"

resp = requests.get(addr)
html = resp.content
soup = bs(html, "html.parser")

row = soup.find_all("tr", "election_item")

election_id = []
election_years = []

for each in row:
	election_id.append(each.get("id").split('-')[2])
	election_years.append(each.contents[1].contents[0])

ELECTION_ID = list(zip(election_id, election_years))

line = zip(election_id, election_years)

ELECTION_ID_file = open('ELECTION_ID.txt', 'w')
for line in ELECTION_ID:
    ELECTION_ID_file.write(line[0] + ' ' + line[1] + '\n')
    print(line[0],line[1])

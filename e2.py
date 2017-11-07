#!/usr/bin/env python
import requests


for line in open("ELECTION_ID.txt"):

	line = line.rstrip('\r\n')
	
	eid = line.split(' ')[0]
	year = line.split(' ')[1]


	addr_pattern = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"
	addr = addr_pattern.format(eid)
	resp = requests.get(addr)

	file_name = "president_general_" + year + ".csv"

	with open(file_name, "w") as out:
		out.write(resp.text)
		print(resp.text)
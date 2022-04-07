# Database Search tool
* language : python3
* required : pymongo, a working mongo database

Searching tool for nested-structure dictionary
____

## Purpose(2022/04/07 edit)
This is my first practice project when I started my position as an RA in NTU Wireless and Mobile Networking Laboratory.

The topic was how to interact with database and json-stucture data, meanwhile I attempted to make my study process into a github project and develope my code in more mature fasion (ofcourse, upon reviewing my work a year after, these code is not that mature and refined).

This was the first time managing a repo and I didn't understand the importance of testing and backups. Many of my learning progression was not recorded and some thought process was missing in the pepo. I've learned the experience from this exercise and eventually changed my way of coding.


## Usage

	import search.py

### Functions

	db_search(coll, target_keys, start = 0, size = 100, index_include = [], index_exclude = ["_id"], filter_keywords = {})

>1.		coll : database collection
>2. 	target_keys : list of string, the keys you wish to search
>3. 	start, size : starting point and the size to search
>4. 	index_include : specify which index(es) to search
>5. 	index_exclude : specify which index(es) not to search
>6. 	filter_keywords : grok style filter

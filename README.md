# Database Search tool
* language : python3

Searching tool for nested-structure dictionary
____

## Usage

	> import search.py

### Functions

	> db_search(coll, target_keys, start = 0, size = 100, 
		index_include = [], index_exclude = ["_id"], filter_keywords = {})

		1. coll : database collection
		2. target_keys : list of string, the keys you wish to search
		3. start, size : starting point and the size to search
		4. index_include : specify which index(es) to search
		5. index_exclude : specify which index(es) not to search
		6. filter_keywords : grok style filter

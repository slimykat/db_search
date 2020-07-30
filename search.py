import pymongo

def nest_flatten(dict_object, parrent = "", sep = "_"):
	new_dict = {}
	for key,value in list(dict_object.items()):
		#new_key = parrent + sep + key if(parrent) else key
		new_key = key
		#print(new_key)
		#print(type(value))
		if(type(value) == dict):
		   new_dict.update(nest_flatten(value, parrent = new_key))
		else:
		   new_dict.update({new_key:value})
	return new_dict


def db_search(coll, target_keys, start = 0, size = 100,
	index_include = [], index_exclude = ["_id"], filter_keywords = {}):
	#find({filtered index:"value"},{expected index:bool, ...})

	filter_index = dict.fromkeys(index_exclude,0).update(dict.fromkeys(index_include,1)) # merge dict
	search_result = []
	for line in coll.find(filter_keywords,filter_index)[start:size]:
		entry = nest_flatten(line)
		
		if any (key in entry for key in target_keys):
		#if all (key in entry for key in target_keys):
			search_result.append(line)

	return search_result

if __name__ == '__main__':
	print("\nusage:")
	print("db_search(collection, target_keys, start, size, filter_keywords = {grok format})", end = "\n\n")



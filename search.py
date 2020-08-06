import pymongo

def get_keys(flat):
    
	name_tags = set()
	for entry in list(flat.keys()):
	    tags = entry.split(".")
	    for tag in tags:
	        name_tags.add(tag)
	return name_tags

def nest_flatten(dict_object, parrent = "", sep = ".", ChangeName = True):
	new_dict = {}
	for key,value in list(dict_object.items()):
		new_key = (parrent + sep + key if(parrent) else key) if(ChangeName) else key
		#print(new_key)
		#print(type(value))
		if(type(value) == dict):
		   new_dict.update(nest_flatten(value, parrent = new_key))
		else:
		   new_dict.update({new_key:value})
	return new_dict


def db_search(coll, target_keys, changename,
	index_include = [], index_exclude = ["_id"], filter_keywords = {}, slimit=10 ):
	#find({filtered index:"value"},{expected index:bool, ...})

	filter_index = {**dict.fromkeys(index_exclude,0), **(dict.fromkeys(index_include,1))} # merge dict
	search_result = []
	for line in coll.find(filter_keywords,filter_index).limit(slimit):
		flat = nest_flatten(line, ChangeName=changename)
		keys = get_keys(flat)
		if (any (key in entry for key in target_keys) or len(target_keys) ==0 ):
		#if all (key in entry for key in target_keys):
			search_result.append(line)

	return search_result

if __name__ == '__main__':
	print("\nusage:")
	print("db_search(collection, target_keys, start, size, filter_keywords = {grok format})", end = "\n\n")



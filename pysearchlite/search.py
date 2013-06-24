from . import indexer

class Search:
	'''Searches a index

		Keyword arguments:
		needle (required) -- keywords to be searched @type: str
		index  (required) -- a valid pysearchlite.indexer.Index class object
	'''

	def __init__(self,needle,index):
		'''@args - index->Index object, needle->string to search for in index'''
		assert type(index) == type(indexer.Index('.')), 'index -> Index object'
		assert type(needle) == type(''), 'needle -> string'
		self.needle_list = []
		self.result_dict = {}
		self.__filter_needle(needle)
		self.__search(index)
		

	def __search(self,index):
		'''Performs the Core function of populating the result dictionary'''
		assert len(self.needle_list) != 0, 'nothing to be searched'
		print("Search for: "+str(self.needle_list))
		for word in self.needle_list:
			#get list of paths for each word in needle
			path_list = index.search_index(word)
			print(word+' is in file(s) '+str(path_list))
			#path -> count
			for path in path_list:
				try:
					self.result_dict[path] += 1
				except KeyError:
					self.result_dict[path] = 1


	def get_search_result(self):
		'''returns result_dict attribute'''
		return self.result_dict

	def __filter_needle(self,needle):
		'''filter needle string of unwanted tokens
		   returns a list of tokens -> needle_list
		   ['token1','token2','token3',...] - 
		   each token must be lower, one can filter here words such as ('a','the',...)
		'''
		needle_list = str.split(str.lower(needle),' ')
		for needle in needle_list:
			if str.strip(needle) != '':
				self.needle_list.append(needle)


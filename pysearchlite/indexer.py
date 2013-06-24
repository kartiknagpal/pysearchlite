import os
import re
from . import PersistentDict

class Index:
	'''Populates a index for files to be searched

		Keyword arguments:
		dir_to_index_path (required) -- valid path to directory which is to be indexed  @type: str
		save_index_path (optional)	 -- valid path to directory where index is to be saved  @type: str
		filetype (optional)		     -- filetypes to be indexed  @type: tuple
		index_mode (optional)		 -- indexing mode i.e to be used @type: str
										# r=readonly, c=create, or n=new

	'''
	def __init__(self,dir_to_index_path,filetype=(),index_mode='n'):
		assert type(dir_to_index_path) == type('')
		assert type(filetype) == type(())
		assert os.path.isdir(dir_to_index_path), 'dir_to_index_path -> must be directory'

		#instance variables used in entire class
		self.dir_to_index_path = dir_to_index_path	#path of the directory to be indexed
		self._save_index_path = ''
		self.index_filename = ''
		self.filetype = filetype

		self.__set_paths()
		self.index = PersistentDict.PersistentDict(os.path.join(self._save_index_path,self.index_filename), \
			format='json', flag=index_mode)

		if index_mode == 'n':
			self.__create_index(self.filetype)

	def __set_paths(self):
		'''__set_paths(self) - Internal function, sets path instance variables for :
			self._save_index_path, self.index_filename
			raises exceptions for Invalid paths
		'''
		#test primary condition on dir_to_index_path
		if os.path.isdir(self.dir_to_index_path) :

			self.dir_to_index_path = os.path.abspath(self.dir_to_index_path)
			self.index_filename = os.path.split(self.dir_to_index_path)[-1] + " (pysearchliteIndex)"
			temp_path = os.path.dirname(self.dir_to_index_path)

			if os.path.isdir(temp_path) :
				self._save_index_path = temp_path
			else:
				raise IOError('Index could not be saved at' + temp_path)
		
		else:
			raise IOError('Invalid path : dir_to_index_path ->' + dir_to_index_path)
		
		# print('dir to index -> '+self.dir_to_index_path)
		# print('save path -> '+self._save_index_path)
		# print('index_filename -> '+self.index_filename)

	def __create_index(self,filetype,rejected_tokens=()):
		'''__create_index(self,filetype,rejected_tokens=(' ',)) - creates index as well as sync it'''
		pattern = re.compile(r'[\w\']+')
		for (root,subs,files) in os.walk(self.dir_to_index_path):
			for f in files:
				#either filetype is empty(everything is indexed), or f endswith one of filetype
				if (not filetype) or (os.path.splitext(f)[1] in filetype):
					#list_of_tokens = str.split(os.path.splitext(f)[0].lower(),' ')
					list_of_tokens = pattern.findall(os.path.splitext(f)[0].lower())
					for token in list_of_tokens:
						if token in self.index:
							#print(token, ' -> ', self.index[token])
							#self.index[token].append(os.path.join(root,f))
							self.index[token].append(f)
						else:
							#print(token , ' -> ', 'new entry')
							#.self.index[token] = [os.path.join(root,f)]
							self.index[token] = [f]
		#write to disk
		self.index.sync()


	def search_index(self,token):
		'''search_index(self,word) -> list of paths from the index'''
		try:
			return self.index[token]
		except KeyError:
			return []


import os
import re
from PersistentDict import PersistentDict

class Index:
	'''Populates a index for files to be searched'''
	def __init__(self,dir_to_index_path,save_index_path='dir_to_index_path',filetype=(),index_mode='n'):
		assert type(dir_to_index_path) == type('') and type(save_index_path) == type('')
		assert type(filetype) == type(())
		assert os.path.isdir(dir_to_index_path), 'dir_to_index_path -> must be directory'

		self.dir_to_index_path = dir_to_index_path	#path of the directory to be indexed
		self.save_index_path = dir_to_index_path #path of the directory where created index would be pickeled
		self.index_filename = ''
		self.filetype = filetype

		self.__set_paths()
		self.index = PersistentDict(os.path.join(self.save_index_path,self.index_filename), \
			format='json', flag=index_mode)
		if index_mode == 'n':
			self.__create_index(self.filetype)

	def __set_paths(self):
		'''__set_paths(self) - Internal function, sets path instance variables for :
			self.save_index_path, self.index_filename
			raises exceptions for Invalid paths
		'''
		#test primary condition on dir_to_index_path
		if os.path.isdir(self.dir_to_index_path) :
			#check if save_index_path is other than default
			if self.save_index_path != self.dir_to_index_path:
				#check if save_index_path is path like
				if self.save_index_path.find('/') or self.save_index_path.find('\\') :
					#dir already exists
					if os.path.isdir(os.path.dirname(self.save_index_path)):
						pass
					else:
						try:
							os.mkdir(self.save_index_path)
							#Invalid path
						except OSError:
							raise IOError('Invalid path : save_index_path ->' + self.save_index_path)
					self.save_index_path = os.path.dirname(self.save_index_path)
					self.index_filename = os.path.basename(self.save_index_path)
				else:
					#only filename is entered
					self.index_filename = self.save_index_path
			else:
				#generate a filename, for windows only
				self.index_filename = os.path.dirname(os.path.abspath(self.dir_to_index_path)).split('\\')[-1]+'idx'
		else:
			raise IOError('Invalid path : dir_to_index_path ->' + dir_to_index_path)

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


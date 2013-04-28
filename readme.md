#FileSystem Search

Inspired by apache lucene core, can be used to search files on th e local filesystem.\n

A successful search results is a python dictionary mapping each matched file to its search rank.\n
Example,\n
{ 'file1': search_rank, 'file2': search_rank}
Note: search_rank is calculated by number of search words matched in the filename.

##Usage
index = Index('directory_to_index_path') \n
search = Search('search words',index) \n
search.get_search_result()

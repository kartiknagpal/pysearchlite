#FileSystem Search

Inspired by apache lucene core, can be used to search files on th e local filesystem.

A successful search results is a python dictionary mapping each matched file to its search rank.
Example,
{ 'file1': search_rank, 'file2': search_rank}
Note: search_rank is calculated by number of search words matched in the filename.

##Usage
index = Index('directory_to_index_path')
search = Search('search words',index)
search.get_search_result()

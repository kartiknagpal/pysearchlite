#FileSystem Search

Inspired by apache lucene core, can be used to search files on th e local filesystem.<br/>

A successful search results is a python dictionary mapping each matched file to its search rank.<br/>
Example,<br/>
{ 'file1': search_rank, 'file2': search_rank}<br/>
Note: search_rank is calculated by number of search words matched in the filename.

##Usage
index = Index('directory_to_index_path') <br/>
search = Search('search words',index) <br/>
search.get_search_result()

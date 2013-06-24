'''
  Example Usage pysearchlite package.
'''

from pysearchlite import *

index = indexer.Index('.',filetype=('.py',), index_mode='n')

search = search.Search('indexer',index)
print('Result: '+str(search.get_search_result()))

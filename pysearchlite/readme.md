#FileSystem Search

Inspired by apache lucene core, this package can be used to search files on the local filesystem.<br/>

A successful search results is a python dictionary mapping, each matched file to its search rank.<br/>
Example,<br/>
{ 'file1': search_rank, 'file2': search_rank}<br/>
Note: search_rank is calculated by number of search words matched in the filename.

##General Usage

index = Index(dir_to_index_path, filetype, index_mode) <br/>
search = Search(search words,index) <br/>
search.get_search_result()

##example usage
```python
from pysearchlite import *

index = Index('.',filetype=('.py',), index_mode='n')	#indexes all python files in the current directory in which this module resides
search = Search('search',index)		#searches for keyword 'search' in the index
print(search.get_search_result())	#prints the result

#output:
#Search for: ['indexer']
#indexer is in file(s) ['indexer.py']
#Result: {'indexer.py': 1}
```

##example usage
```python
from pysearchlite import *

index = indexer.Index('d:\\Ent',filetype=('.mp4','.avi','.mkv'), index_mode='n')

search1 = search.Search('ice age',index)
print('Result: '+str(search1.get_search_result()))

search2 = search.Search('iron man',index)
print('Result: '+str(search2.get_search_result()))

#output:
#Search for: ['ice', 'age']
#ice is in file(s) ['Ice Age 2002.mp4', 'Ice Age 2006 The Meltdown.mp4', 'Ice Age 2009 Dawn Of The Dinosaurs.mp4', 'Ice Age 2011 A Mammoth Christmas.mp4', 'Ice.Age.Continental.Drift.2012.720p.BluRay.x264.YIFY.mp4', 'Thin.Ice[2011]BDRip.720p[Eng]-Junoon.mkv']
#age is in file(s) ['Ice Age 2002.mp4', 'Ice Age 2006 The Meltdown.mp4', 'Ice Age 2009 Dawn Of The Dinosaurs.mp4', 'Ice Age 2011 A Mammoth Christmas.mp4', 'Ice.Age.Continental.Drift.2012.720p.BluRay.x264.YIFY.mp4']
#Result: {'Ice Age 2002.mp4': 2, 'Ice Age 2009 Dawn Of The Dinosaurs.mp4': 2, 'Ice Age 2011 A Mammoth Christmas.mp4': 2, 'Ice Age 2006 The Meltdown.mp4': 2, 'Thin.Ice[2011]BDRip.720p[Eng]-Junoon.mkv': 1, 'Ice.Age.Continental.Drift.2012.720p.BluRay.x264.YIFY.mp4': 2}
#Search for: ['iron', 'man']
#iron is in file(s) ['Iron Man 2 2010 720p  BRRiP Dual Audio Hindi Eng[Sub]--ChEtAn.mkv']
#man is in file(s) ['Inside Man(2006).480P.BRRip.H264.ResourceRG by Dusty.mp4', 'Iron Man 2 2010 720p  BRRiP Dual Audio Hindi Eng[Sub]--ChEtAn.mkv', 'Man.on.a.Ledge.2012.720p.BluRay.x264.YIFY.mp4']
#Result: {'Iron Man 2 2010 720p  BRRiP Dual Audio Hindi Eng[Sub]--ChEtAn.mkv': 2, 'Man.on.a.Ledge.2012.720p.BluRay.x264.YIFY.mp4': 1, 'Inside Man(2006).480P.BRRip.H264.ResourceRG by Dusty.mp4': 1}
#[Finished in 0.6s]
```

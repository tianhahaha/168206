# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 18:13:51 2018

@author: 程甜甜
"""


start ="hit"
end = "cog"
adict = ["hot","dot","dog","lot","log"]
def link(a,b):
	n=len(a)
	same=0
	for i in range(n):
		if a[i]==b[i]:
			same+=1
	if same==n-1:
		return True
	else:
		return False
suc=[]
path=[]
path.append(start)
def searchPath(path):
	n=len(path)
	for d1 in adict:
		if link(path[-1],d1):
			if(d1 in path):
				pass
			else:
				path.append(d1)
				if link(d1,end):
					path.append(end)
					suc.append(path)
					break;
				searchPath(path)
		path=path[:n]		
searchPath(path)
for s in suc:
    print(len(s),s)
    #print(s)
    
    #link(path[-1],d1) 这里不知道为什么是-1
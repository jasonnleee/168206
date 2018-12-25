def indegree0(v,e): 
 	if v==[]:
 		return None
 	tmp=v[:]
 	'''寻找入度为0的，放在tmp中'''
 	for i in e:
 		if i[1] in tmp:
 			tmp.remove(i[1])
 	if tmp==[]:
 		return -1
 	'''删除入度为0 的链接线'''
 	for t in tmp:
 		for i in range(len(e)):
 			if t in e[i]:
 				e[i]='toDel' #占位，之后删掉
 		#tmp.remove(t)
 	
 	if e:
 		eset=set(e)
 		eset.remove('toDel')
 		e[:]=list(eset)
 	
 	if v:
 		for t in tmp:
 			v.remove(t)
 	
 	return tmp
def topoSort(v,e):
 	result=[]
 	while True:
 		nodes=indegree0(v,e)
 		if nodes==None:
 			break
 		elif nodes==-1:
 			print('there\'s a circle.')
 			return None
 		result.extend(nodes)
 	return result
v=['a','b','c','d','e']
e=[('a','b'),('a','d'),('b','c'),('d','c'),('d','e'),('e','c')]
res=topoSort(v,e)
print(res)

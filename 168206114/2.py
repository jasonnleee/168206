start = 'hit'
end = 'cog'
adict = ['hot','dot', 'hi', 'dog', 'lot', 'loc', 'log']
def Message(arr,left,eight):
	mid = len(arr)/2
	mid = int(mid)
	if left == mid or mid == eight:
		if arr[left-1] > arr[eight-1]:
			arr[left-1],arr[eight-1] = arr[eight-1],arr[left-1]
		return arr
	else:
		arr1 = Message(arr[:mid],left,mid)
		a = int(eight) - int(mid)
		arr2 = Message(arr[mid:],left,a)
		return sorf(arr1,arr2)

def sorf(arr1,arr2):
	arr = []
	while len(arr1)!=0 and len(arr2)!=0:
		if arr1[0] >= arr2[0]:
			arr.append(arr2.pop(0))
		else:
			arr.append(arr1.pop(0))
	if len(arr1)==0:
		for i in range(0,int(len(arr2))):
			arr.append(arr2[i])
	else:
		for i in range(0,int(len(arr1))):
			arr.append(arr1[i])
	return arr
'''上为 用快速排序将 adict 列表排序'''

def chazhao(adict, start):
	
adict1 = Message(adict, 0, len(adict))
print(adict1)

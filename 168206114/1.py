thief = ['A','B','C','D']

print("小偷是：",end="")
for s in thief:
	i = s  
	A=(i != 'A')
	B=(i == 'D')
	C=(i == 'B')
	D=(i != 'D')
	if (A + B + C + D == 1):
		lists = [A,B,C,D]
		print(i,end=" ")
		print("\n说真话的是：",end="")
		for i in range(len(lists)):
			if lists[i]:
				print(thief[i],end=" ")

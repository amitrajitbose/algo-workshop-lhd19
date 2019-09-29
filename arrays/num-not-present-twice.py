def getNumber(arr):
	n = len(arr)
	x = arr[0]
	for i in range(1,n):
		x = x ^ arr[i]
	return x

print(getNumber([1,2,3,3,2]))

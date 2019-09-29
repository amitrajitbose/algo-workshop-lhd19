def find_missing_number(arr):
	n = len(arr)
	n += 1
	expectedsum = (n*(n+1))//2
	originalsum = sum(arr)
	return expectedsum - originalsum

print(find_missing_number([1,3,4,5]))

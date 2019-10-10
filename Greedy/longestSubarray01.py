'''
Longest Contiguous Zero - One Subsequence (Subarray)
Given an array, find the largest subarray with equal number 
of 0's and 1's and print the length and start index and end index of the largest subarray
'''
# Author: @amitrajitbose

def longSeq(arr):
	glen=-1
	l=len(arr)
	for i in range(l-1):
		lsum=0
		if(arr[i]==0):
			lsum=-1
		else:
			lsum=1
		for j in range(i+1,l):
			if(arr[j]==1):
				lsum+=1
			else:
				lsum-=1
			if(lsum==0):
				#got a subarray of equal zero and ones
				if((j-i+1)>glen):
					glen=j-i+1
	return glen

def main():
	print(longSeq([1,0,0,1,1,1])) #4
	print(longSeq([1,1,1,0,0,0,1,0,1,0])) #10
	print(longSeq([1,0,1,1,0,0,1,1,1,1])) #6
	input()

main()
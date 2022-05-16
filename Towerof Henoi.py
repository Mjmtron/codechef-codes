def rope(n,a,b,c):
	if n==0:
		return 0
	if n<0:
		return -1
	if n>0:
		result=max(rope(n-a,a,b,c),rope(n-b,a,b,c),rope(n-c,a,b,c))
		return (result+1)
	
n,a,b,c=map(int,input().split(" "))
print("max no. of pices=",rope(n,a,b,c))
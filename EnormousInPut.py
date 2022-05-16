ans=0
n,k=map(int,input ().split (" "))
for i in range (0,n):
	a=int(input(f"enter no. {i+1}="))
	if (a%k==0):
		ans+=1
print(ans)


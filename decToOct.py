n=int(input("enter no."))
j=[]
a=0
while( n>0):
	i=n%8	
	n=n//8
	print(n,"%8=",i)
	a+=1
	j.insert(a,i)
k=j[::-1]
print (k)


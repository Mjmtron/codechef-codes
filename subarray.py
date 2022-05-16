l= [] 
x=int(input ("enter no. of elementsto be inserted:\t"))
for i in range (x):
	d=int(input ("enter no."))
	l.append(d)
a=[]
for i in range (len(l)):
	for j in range(i, len(l)):
		for k in range(i, j+1):
			print(l[ k ]," ",end=" ")
			a.append (l[k])		
		print(" ")	
	print(" ")
print(a)

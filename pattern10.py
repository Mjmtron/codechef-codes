a=1
for row in range (6,0,-1):
	for col in range (row):
		print(a%2,end="	")	
		a+=1
	print("\n")
	
import numpy as np
#taking input of number of rows in square matrix

row=int(input("enter row of ■ matrix :	"))

#defineing matrix

M=np.zeros((row,row))

#defineing pointers
top,right,base,left=0,len(M[0]),len(M),0	

while ((left<right) and (top<base)):
#traveling on 👆top of matrix 		
		for i in range(left,right):
			M[top][i]=int(input(f"{top,i}enter no.  "))
		top+=1
#traveling on 👉 right of matrix		
		for i in range(top,base):
			M[i][right-1]=int(input(f"{i,right-1}enter no.  "))	
		right-=1
		
	#	if((left<right) and (top<base)):
	#		break
			
#traveling on 👇base of matrix 		
		for i in range(right-1,left-1,-1):
			M[base-1][i]=int(input(f"{base-1,i}enter no.  "))
		base-=1
#traveling on left👈 of matrix		
		for i in range(base-1,top-1,-1):
			M[i][left]=int(input(f"{i,left}enter no.  "))	
		left+=1
#printing matrix 😎 
print("\n\n\n")
for i in M:
	print(i)

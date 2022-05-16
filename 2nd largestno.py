#taking input for number of integers in which we have to find 2nd largest integer 
number_of_integers=int(input ("enter number of integers you want to enter to find 2nd largest integer\n:\t"))
#highest positve integer is zero
highest_positve_integer=0

#repetedly we have to take integers from program operater
for i in range(number_of_integers):
	integer=int(input(f"enter number \t"))
	print(i,":    ")
	#finding 2nd largest integer
	#if input given by user is higher than the highest positve integer 
	if integer>highest_positve_integer:
		#then new integer is largest integer 
		# and the last largest integer is 2nd highest
		second_highest_positve_integer=highest_positve_integer
		highest_positve_integer=integer		
#printing the output
print(f"second largest integer is {second_highest_positve_integer}")		
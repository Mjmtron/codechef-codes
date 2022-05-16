#taking decimal input
Decimal=int(input("\nenter decimal number:\t"))
decimal=Decimal

#our binary output is empty currently
binary_output=""
#dividing decimal until decimal is equal to 1
while( Decimal>0):
	#adding remainder after 2s division
	binary_output+=str(Decimal%2)	
	#dividing decimal by 2
	Decimal=Decimal//2

print(f"\n\nbinary of {decimal} is {binary_output[::-1]}\n\n")



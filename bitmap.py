#bitmap is used to trace a string on pattern
#in this program heart is the pattern
import sys
#creating bitmap
bitmap="""
  ***          ***
  ******    ******
   *************
    ***********
      ********
       *****
         *"""
#taking user input of string
print("type your name ")
string_input=input(">...")
#if input is empty then exit the program
if string_input=='':
 sys.exit()
#changing * with the input string
for line in bitmap.splitlines():
 		for i, bit in enumerate(line):
 			if bit == ' ':
 				print(' ', end='')
 			else:
 				print(string_input[i % len(string_input)], end='')
 		print()
 		
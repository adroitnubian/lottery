#!C:\Python27\python.exe
# _*_ coding: UTF-8 _*_
#

#	Date		Author		Description
#	28/02/2019	MAC			Initial version
#	28/02/2019	MAC			Remove comments
#
############################################################
import os
import random

def main():
	numbers = [0] * 6
	for i in range(6):
		numbers[i] = random.randint(1, 59)
#		print (numbers[i], end=' ')
		print numbers[i],


# Call the main function.
#main() 
if __name__ == "__main__":
    # Execute only is run as a script
    main()

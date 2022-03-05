# *************************************************
# *  321 Programming Languages                    *
# *  Fall 2021                                    *
# *  Author: Yunus Emre Geyik                     *
# *  File  : exponent_[1801042635].py             *
# *                                               *
# *  Finds Exponent a Number Two Differen Method. * 
# *************************************************


# In this function i used the Brute-Force Algorithm for the find exponent of an integer
def exponent_BF( base, exponent):
	result=1               # result variable initially 1 

	if (exponent == 0):             # if the exponent is 0, then the result is 1
		return 1

	if (base == 0):                 # if the base is 0, then the result is 0
		return 0    

	# So as Brute-Force Technique wants us,  	
	# In this part of function i iterate 0 to exponent number and i multiply the result with base in each iteration.
	for i in range(0,exponent):
		result = result * base

	return result                      # return the result	

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# In this function i used the Divide and Conquer Algorithm for the find exponent of an integer
def exponent_DAC( base, exponent):
	half=0                      # half value using for the division and initially zero

	if (exponent == 0):			 # if the exponent is 0, then the result is 1
		return 1

	if (base == 0):				# if the base is 0, then the result is 0
		return 0 

	# So as Divide and Conquer Technique wants us,
	#  Divide the problem into sub problems with size exponent/2 and solve it recursively.
	half =  exponent_DAC( base, int(exponent / 2))

	if(exponent % 2 == 0):		# if the the exponent is even then result is multiply of halfs
		return half * half
	else :								# if the the exponent is odd then result is multiply of halfs and base					
		return half * half * base

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Driver Code
if __name__ == "__main__":

	base= 2
	exponent= 5

	print ("Base : {}".format(base))
	print ("exponent : {}".format(exponent))

	result_BF=exponent_BF( base, exponent)

	print("Exponent Problem With Bruth-Force : {} \n ".format(result_BF))

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

	base= 3
	exponent= 3

	print ("Base : {}".format(base))
	print ("exponent : {}".format(exponent))

	result_DAC=exponent_DAC( base, exponent)
	print("Exponent Problem With Dicide and Conquer : {} ".format(result_DAC))
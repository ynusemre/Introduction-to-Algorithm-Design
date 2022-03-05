# *********************************************
# *  321 Programming Languages                *
# *  Fall 2021                                *
# *  Author: Yunus Emre Geyik                 *
# *  File  : candy_[1801042635].py            *
# *                                           *
# * Finds the maximum obtainable value.       * 
# *********************************************

import sys

# This code finds the maximum obtainable value using via dynamic programming algorithm.

def FindMaxObtainable( arr, candyLength):
    

    temp_arr = [0]*(candyLength+1)   # a temporary array is filled with 0 for the length of the given array.
    
   	# this loop iterate 1 index of given array to last index + 1. So length of the candy
    for i in range(1, candyLength+1):
        # for each of the outer loop maxObtainable assign the max negative number for the comparison.
        maxObtainable = -sys.maxsize          
        
        # this inner loop j to i index.
        for j in range(i):
        	# using via buttom to up method,
        	# By iterating through the array, code add The values of the array given to the function as a parameter up to 
        	# the index value of the outer loop and the values of the temporarily created array from 
        	# the index value of the outer loop to the 0th index value are added.
        	
        	# and with the result we get, we assign the maxObtainable variable, whichever is greater than the current maxObtainable.
            maxObtainable = max(arr[j] + temp_arr[i-j-1], maxObtainable)
        
        # The variable maxObtainable is assign to the index value i of the temporary array in the outer loop.
        temp_arr[i] = maxObtainable             

    return temp_arr[candyLength]   # return the last value of the temp_arrr

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Driver code
if __name__ == "__main__":
		
	lengths=[1, 2, 3, 4, 5, 6, 7, 8]				# pieces lengths
	prices = [1, 5, 8, 9, 10, 17, 17, 20]  			# array example
	candyLength=8                                  # length of the candy

	print ("The Lengths :{} ".format(lengths))
	print ("The Prices : {} ".format(prices))
	print ("Length of The Candy : {} \n".format(candyLength))

	

	maxObtainable=FindMaxObtainable( prices, candyLength)
	print("The maximum profit : {}".format(maxObtainable))
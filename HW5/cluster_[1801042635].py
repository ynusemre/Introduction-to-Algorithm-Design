# **********************************************************************
# *  321 Programming Languages                                         *
# *  Fall 2021                                                         *
# *  Author: Yunus Emre Geyik                                          *
# *  File  : cluster_[1801042635].py                                   *
# *                                           						   *
# * Finds the maximum profit belonging to the most profitable cluster. * 
# **********************************************************************



# This code finds the the maximum profit cluster using via dynamic programming algorithm.

def findMaxProfit( arr):
    
    length=len(arr)				# lenght of array
    maxProfit =arr[0]			# max profit initially first element of array
    tempMaxProfit = arr[0]		# temporary max profit variable initially first element of array
    
    for i in range(1,length):						# loop going to 1 index to the last index
        # By iterating through the array, code add the current array element to the value of the tempMaxProfit variable, 
        # and with the result we get, we assign the tempMaxProfit variable, whichever is greater than the current element.
        tempMaxProfit = max(tempMaxProfit + arr[i], arr[i])             
        
        #  If tempMaxProfit is greater than maxProfit, update maxProfit equals to tempMaxProfit.
        maxProfit = max(tempMaxProfit, maxProfit)
        
    return maxProfit

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Driver code
if __name__ == "__main__":
	
	arr = [3, -5, 2, 11, -8, 9, -5]       # array example
	

	print ("The Array : {} \n".format(arr))

	maxProfit=findMaxProfit(arr)
	print("The maximum profit : {}".format(maxProfit))





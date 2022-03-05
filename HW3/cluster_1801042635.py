import sys

# This method finds the maximum profit that belongs to the most profitable cluster using via divide and conquer
def findMaxProfit(arr, low, high):

	# if array has just one element
	if (low == high):
		return arr[low]

	# middle point of array
	middle = (low + high) // 2

	#left sub array start at the initial point of array and end the middle point of array
	leftSum=findMaxProfit(arr, low, middle)   # find the left sub array's max profit
	
	#right sub array start at the middile+1 point of array and end the high point of array
	rightSum=findMaxProfit(arr, middle+1, high)   # find the right sub array's max profit
	
	#using with helper method, merge the right and left sub array 
	mergeSum=mergeSubArrays(arr, low, middle, high)  # find the merge array's profit 

	maxProfit=max(leftSum,rightSum,mergeSum)

	return maxProfit    # evaluate the all possible max profit and return maximum of them

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

def mergeSubArrays(arr, low, middle, high):
	sum = 0
	leftSum = -sys.maxint    # The smallest obtainable integer number is initially assigned to leftSum. It is used to find the max sum.
	
	#Starting from the middle point of the left sub-array to the starting point, at each point, 
	#the maximum total is tried to be found from that point to the starting point 
	#and it is assigned to the value lef_sum.
	
	for i in range(middle, low-1, -1):
		sum = sum + arr[i]

		if (sum > leftSum):
			leftSum = sum

	sum = 0
	rightSum = -sys.maxint    # The smallest obtainable integer number is initially assigned to rightSum. It is used to find the max sum.
	
	#Starting from the middle+1 point of the right sub-array to the ending point, at each point, 
	#the maximum total is tried to be found from that point to the ending point 
	#and it is assigned to the value rightSum.

	for i in range(middle + 1, high + 1):
		sum = sum + arr[i]

		if (sum > rightSum):
			rightSum = sum

	
	mergeSum=leftSum + rightSum   #The max total values obtained in the divides right and left subarray are summed
	
	return max(mergeSum, leftSum, rightSum)    #The largest of the three possibilities is returned.

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Driver code
if __name__ == "__main__":

	arr = [3, -5, 2, 11, -8, 9, -5]      # array example
	n = len(arr)                         # lenght of array

	maxProfit=findMaxProfit(arr, 0, n-1)
	print(" The maximum profit : {}".format(maxProfit))
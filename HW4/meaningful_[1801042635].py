# *********************************************
# *  321 Programming Languages                *
# *  Fall 2021                                *
# *  Author: Yunus Emre Geyik                 *
# *  File  : meaningful_[1801042635].py 	  *
# * 										  *
# *  Finds k'th Meaningful Rate.		      * 
# *********************************************

# This method finds the k'th meaningful rate in the success rates withoud sorting
# And it using decrease and conquer technique

def kthMeaningful( rates, first, last, k):
	if (k > 0 and k <= last - first + 1):	          # Control for the if wanted k index is out of size of array

		# Determine the pivot pos using via Lomuto Partition function
		pos = LomutoPartition(rates, first, last)
		
		if ( pos == first + k - 1):          # If pivot pos is the k'th meaningful element then return the pos index value directly
			return rates[pos]
		

		# if the k'th meaningful element is the k'th meaningful of the left part
		# recursive call using for the left sub array
		# first value is initial first index and the last value is pos - 1 index 
		# k'th meaningful also left sub array k'th meaningful
		if ( pos - first > k - 1): 									
			return kthMeaningful( rates, first, pos - 1, k)  

		# if the k'th meaningful element is the k'th meaningful of the right part
		# recursive call using for the right sub array
		# first value is pos + 1 index and the last value is initial last index
		# k'th meaningful is not right sub array k'th meaningful
		# i send the k-pos-1+first index instead of k'th 
		return kthMeaningful( rates, pos + 1, last, k - pos - 1 + first)   
	
	else :                   # if the k'th index out of size then return 0
		return 0
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#	


# It considers the last element as pivot and
# moves all smaller element to left of it
# and greater elements to right
def LomutoPartition( rates, first, last):

	p = rates[last]                  # pivot select as last element of the array
	
	# split position of the partition
	s = first						 # that's a virtual pointer using for the swap operation when elements arrages according to pivot 
	
	for i in range( first, last ):
		
		if ( rates[i] <= p ):						# if pivot bigger than array element
			rates[s], rates[i] = rates[i], rates[s]				# swap the array element and virtual pointer
			s = s + 1											# increment pointer index by one
	# at the end of the for operation
	# swap the pivot element and pointer and put the pivot element its actual position if the array ordered by inceasing
	rates[s], rates[last] = rates[last], rates[s]           
	
	# and return the pivot element index 
	return s

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Driver Code
if __name__ == "__main__":
	
	n=11     # Number of experiment
    
	rates = [51, 18, 21, 45, 10, 8, 19, 48, 34, 29, 11]   #success_rates
	
	k = 3;
	
	print(" The array size : {} ".format(n))
	print(" The Success Rates array as % : {} ".format(rates))
	print(" Wanted k^th meaningful experiment : {} \n".format(k))

	
	meaningful=kthMeaningful(rates, 0, n-1, k)
	
	print("The success rate of the first meaningful k^th experiment: {} ".format(meaningful))
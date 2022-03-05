# ***********************************************
# *  321 Programming Languages                  *
# *  Fall 2021                                  *
# *  Author: Yunus Emre Geyik                   *
# *  File  : find_rop_[1801042635].py 	        *
# * 										    *
# *  Finds the number of reverse ordered pairs. * 
# ***********************************************


# This function finds the number of reverse ordered pairs using via divide and conquer method
# The main idea is divide the given array to the two sub array and calculate their number of reverse ordered pairs
# Then merge two sorted array and create a new sorted array and calculate its number of reverse ordered pairs
# Then add and return the three possible cases number of reverse ordered pairs
def sort_and_count(arr, aux_arr, first, last):
	counter = 0   # this counter holds the number of reverse ordered pairs for 3 possibilty 

	if ( first < last ):   # if the given array more then one element

		
		# the middle point find and will using the divide the array
		# // operator is using for the floor division
		middle = (first + last) // 2

		# In this recursive calls code calculate the reverse ordered pair in the left sub array and sort the array
		counter = counter + sort_and_count( arr, aux_arr, first, middle)

		# In this recursive calls code calculate the reverse ordered pair in the right sub array and sort the array
		counter = counter + sort_and_count( arr, aux_arr, middle + 1, last)

		# using via helper function merge and count,
		# merge two sorted sub arrays and create a new array then return the number of reverse ordered pair in this new array
		counter = counter + merge_and_count( arr, aux_arr, first, middle, last)
	
	return counter   # then return the all reverse ordered pair number for the three possible situation

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# This function merges two sorted sub arrays and create a sorted array with using them
def merge_and_count(arr, aux_arr, first, middle, last):

	# i like a pointer and traversel in the left sub array of the given array
	i = first	

	# j like a pointer and traversel in the left sub array of the given array
	j = middle + 1

	# k like a pointer and traversel in the new sorted sub array which creating with sub arrays
	k = first	
	counter = 0      # this counter holds the reverse ordered pairs number 

	
	# this loop going to till left sub array's pointer i arrive the middle index 
	# and right sub array pointer arrive the last index

	# This while loop control the each sub array and compare their value and find the reverse ordered pair
	# left sub array value must be bigger than right sub array if there is an inversion

	while ( i <= middle and j <= last ):

		# if the right sub array pointer value bigger then the left sub array pointer value 
		# then put the left sub array value to the new created array
		# and there is no inversion because bigger value must be in the left sub array

		if ( arr[i] <= arr[j] ):
			aux_arr[k] = arr[i]
			k = k + 1
			i = i + 1
		else:

			# if the left sub array pointer value bigger then the right sub array pointer value 
			# then put the right sub array value to the new created array
			# and there is an inversion and increment counter
			# don't look the reaming element of the left sub array because there is also bigger then the right sub array value.
			
			aux_arr[k] = arr[j]
			counter = counter + (middle-i + 1)
			k = k + 1
			j = j + 1

	# If there is no element in the right sub array then copy the left sub array element to the new created array
	while ( i <= middle ):
		aux_arr[k] = arr[i]
		k = k + 1
		i = i + 1

	# If there is no element in the left sub array then copy the right sub array element to the new created array
	while ( j <= last ):
		aux_arr[k] = arr[j]
		k = k + 1
		j = j + 1

	# And after the all operation copy the new created array to the original array
	for i in range( first, last + 1):
		arr[i] = aux_arr[i]
		
	return counter

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Driver Code
if __name__ == "__main__":
	
	arr = [51, 8, 18, 25, 6]                       # given array
	n = len(arr)								   # array size
	
	print(" The array size : {} ".format(n))
	print(" The array : {} \n".format(arr))

	aux_arr= [0]*n   								# a temporary array using for the merge operation and fills the 0 initially
	
	result = sort_and_count(arr, aux_arr, 0, n - 1)
	
	print("The number of reverse ordered pairs : {} ".format(result))
# *********************************************
# *  321 Programming Languages                *
# *  Fall 2021                                *
# *  Author: Yunus Emre Geyik                 *
# *  File  : cheese_[1801042635].py           *
# *                                           *
# *  Finds the maximum price.                 * 
# *********************************************


# Finds the maximum number of price problem solved via Greedy Algortihm.

def FindMaxPrice(cheesePrice, cheeseWeight, boxCapacity):
	length=len(cheeseWeight)                # length of the cheeseWeight array
    
	index = [0]*length                      # an index array holds the cheesePrice's or cheeseWeight's index value (0,1,2...)
	for j in range(0,length):
		index[j]=j

	
    
	# A new array holding the ratios of the cheesePrice and cheeseWeight array elements
	ratio= [0]*length

	for i in range(0,length):
		ratio[i]=cheesePrice[i] / cheeseWeight[i]

	# index is sorted according to cheesePrice and cheeseWeight ratio in decreasing order
	index.sort(key=lambda i: ratio[i], reverse=True)
 	
 	maxPrice = 0                    # maxPrice variable
   	
   	# The loop performs a check from the first index of the index  to the last index of the array. 
   	# Because, thanks to this control, we can understand whether the cheeses can be put in whole and cut form.
	for i in index:
		if (cheeseWeight[i] <= boxCapacity):            # cheese weight is smaller than or equal box capacity 
            
			maxPrice = maxPrice + cheesePrice[i]					# cheese price added to the max price and assign to the maxPrice
			
			# So, box capacity must be decrease because added the cheese
			# Box capacity is reduced by the weight of cheese.
			boxCapacity = boxCapacity - cheeseWeight[i]			
		else:
            # This is the cutting part
            # maxPrice increases as the ratio of box capacity to cheese weight multiplied by the price of cheese.
			maxPrice = maxPrice + (cheesePrice[i]*boxCapacity/cheeseWeight[i])
			break

	return maxPrice     # then return the maxPrice
 
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Driver code
if __name__ == "__main__": 
	cheeseWeight = [10, 70, 20, 30, 80]
	cheesePrice = [60, 50, 100, 120, 20]
	boxCapacity = 50
	
	print ("The Cheeses Weights :{} ".format(cheeseWeight))
	print ("The Cheeses Price :{} ".format(cheesePrice))
	print ("The Box Capacity :{} \n".format(boxCapacity))

	maxPrice= FindMaxPrice(cheesePrice, cheeseWeight, boxCapacity)
	print("The maximum value of items that can be carried : {}".format(maxPrice))
	
	
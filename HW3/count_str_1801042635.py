
def find_counter(first,last,str):

	n=len(str)   # size of all strins

	counter=0	   # counter for the 'X' letter using for determine the 'X' letters index
	counter2=0     # counter for the 'Z' letters
	for i  in str:     # loop for check all string
		
		if(i=='X'):  # if loop meet to letter 'X'
			
			for j in range(counter,n):      # this loop for the find 'Z' letter
				if(str[j]=='Z'):            # find the letter 'Z'
					counter2=counter2+1     # increase 'Z' letters counter
		counter=counter+1                   # increase 'X' letters counter

	return counter2                         # return count of the substrings

# Driver code
if __name__ == "__main__":



	str="TXZXXJZWX"             # String Example

	result=find_counter('X','Z',str)

	print("Counts the number of substrings : {}".format(result))
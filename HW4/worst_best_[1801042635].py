# *********************************************
# *  321 Programming Languages                *
# *  Fall 2021                                *
# *  Author: Yunus Emre Geyik                 *
# *  File  : worst_best_[1801042635].py       *
# *                                           *
# *  Finds Worst and Best Success Rate.       * 
# *********************************************

import sys
 
# I used divide and conquer method for the finds Worst and Best success rate.


# i determine worst value as a maxsize of integer value and best value as maxsize of negative integer for the make comparsion clearly    
def Worst_Best_Rate( rates, first, last, worst=sys.maxsize, best=-sys.maxsize):     
 
    # if the success rate array has only 1 value
 
    if ( first == last):                  # for there is only one value first and last value of the array must be the same
 
        if ( worst > rates[last]):        # if the variable is the smaller than worst value that we determine initially
            worst = rates[last]
 
        if ( best < rates[first]):        # if the variable is the bigger than best value that we determine initially
            best = rates[first]
 
        return worst, best                # for there is only one value worst and best value is the same
 
    # if the success rate array has only 2 value
 
    if ( last - first == 1):           # for there is only 2 value the first and last value of the array subtraction must be the two
 
        if ( rates[first] < rates[last]):      # if the last value of the array bigger than  the first value of the array
            if ( worst > rates[first]):       # if the worst value is bigger than the first value of the array
                
                # then our worst value must be first value of the array 
                # because it is smaller then the worst value that i determine intially and last value of the array
                worst = rates[first]           
 
            if ( best < rates[last]):      # if the best value is smaller than the last value of the array
                
                # then our best value must be last value of the array 
                # because it is bigger then the best value that i determine intially and first value of the array
                best = rates[last]
 
        else:
            if ( worst > rates[last]):      # if the worst value is bigger than the last value of the array
                
                # then our worst value must be last value of the array 
                # because it is smaller then the worst value that i determine intially and first value of the array
                worst = rates[last]
 
            if ( best < rates[first]):       # if the best value is smaller than the first value of the array
                
                # then our best value must be first value of the array 
                # because it is bigger then the best value that i determine intially and last value of the array
                best = rates[first]
 
        return worst, best          # then return the worst and best values which i found with the above comparision
    
    
    # calculate the middle value of the success rate array for the division
    middle = ( first + last) // 2       # i used // operator for the floor division
 
    # In this recurrence relation for the left subarray of the success rates array,
    # I determined first value as the initial first value and last value as the middle value of the array then code call recursively
    worst, best = Worst_Best_Rate(rates, first, middle, worst, best)
 
    # In this recurrence relation for the right subarray of the success rates array,
    # I determined first value as middle + 1 index value of array and last value as the initial last value then code call recursively
    worst, best = Worst_Best_Rate(rates, middle + 1, last, worst, best)
 
    return worst, best   # then return the worst and best values which i found with the above comparision and recursive call
 
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Driver code 
if __name__ == '__main__':
    
    n=11     # Number of experiment
    
    rates = [51, 18, 21, 45, 10, 8, 19, 48, 34, 29, 11]   #success_rates
    
    print(" The array size : {} ".format(n))
    print(" The Success Rates array as % : {} \n ".format(rates))

    # i send the first value as 0 and last value as the lengt of array - 1 to function
    (worst, best) = Worst_Best_Rate(rates, 0, n - 1)        
    
    print("The Worst Success Rate : {} ".format(worst))
    print("The Best Success Rate : {} ".format(best))
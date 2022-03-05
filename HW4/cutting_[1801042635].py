# *********************************************
# *  321 Programming Languages                *
# *  Fall 2021                                *
# *  Author: Yunus Emre Geyik                 *
# *  File  : cutting_[1801042635].py          *
# *                                           *
# *  Finds the minimum number of cuts.        * 
# *********************************************


# I used the decrease and conquer method for the find the minumum number of cuts.
# i used decrease by a constant factor method for the finding min number of cutting.
def CutsWire( wire_length, cuts):
    
    if( wire_length > 1) :              # if wire length bigger than 1 then we can calculate the the minimum number of cuts
        cuts = cuts + 1                     # in each decreasing, the code increment the cuts counter by 1
        
        return CutsWire(wire_length/2.0, cuts)    # i decrease the wire length with constant factor 2
    
    else :
        return cuts       # if the wire length smaller then 1 then cuts return directly 


#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Driver code 
if __name__ == '__main__':
    
    wire_length = 4
    initial_cuts=0


    print("                |----|     ")
    
    print("      |--|                  |--|     (1. cut)")

    print("   |-|     |-|          |-|       |-|  (2. cut)")

    print("The Wire of Length : {} ".format(wire_length))

    min_cuts=CutsWire( wire_length, initial_cuts)

    print("The minimum number of cuts : {} \n".format(min_cuts))

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#


    wire_length = 5
    initial_cuts=0


    print("               |-----|     ")
    
    print("         |---|               |--|     (1. cut) ")

    print("     |--|       |-|      |-|       |-|   (2. cut)")

    print("  |-|     |-|   |-|      |-|       |-|    (3. cut)")

    print("The Wire of Length : {} ".format(wire_length))

    min_cuts=CutsWire( wire_length, initial_cuts)

    print("The minimum number of cuts : {} ".format(min_cuts))  
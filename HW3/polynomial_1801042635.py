
"""
The algorithm finds the values of the degrees of x one by one, 
starting from the highest degree of the polynomial expression to the lowest degree, 
and multiplies it by the coefficient of that degree, does this for all degrees of x and adds them all, 
and the value of the polynomial is reached.
"""

def  polynomial(Coefficients, x):  # parameters are coefficients array and point of x value
	
	sum_value=0 		# initial value of value of polynomial at point x
 	
	n=len(Coefficients)-1  # degree of polynomial expression
	

	for i in range(n,-1,-1) :   # loop starts from last degree of polynomial that n value and decrease by 1
		power=1                 #  power of degree x   
		
		for j in range(i):    # loop going to till i
			power=power*x      #  power of degree x  
		
		sum_value= sum_value + (power * Coefficients[i])     # sum all degrees of x's value and equalize to sum_value
	
	return sum_value	



# Driver code
if __name__ == "__main__":


	# The Polynomial Expression
	#   P= 2 x^3 + 3x^2 + 5x + 9
	# Result= (2 * 2^3) + (3 * 2^2) + (5*2) + (9) = 47


	Coefficients = [9,5,3,2]                         # coefficients of given polynomial
	result=polynomial(Coefficients,2)				 # result is the value of polynomial at the 2 point
	
	print("value of polynomial at the point 2 for x : {}".format(result))					
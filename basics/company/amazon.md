# OA

## Rice bags

Given a list of ricebags, choose a set of perfect ricebags with maximum size. A perfect ricebag set obeys the following conditions:

	1. At least size of 2 
	2. When sorted, ricebags[i]*ricebags[i]=ricebags[i+1] , for all 0<=i<=N(length of ricebags)

Example: ricebags=[3, 4, 2, 9, 16] 
Possible sets are:
	1. [3,9]  -> size=2
	2. [4,2]  -> size=2 
	3. [4,16] -> size=2
	3. [4,2,16]  -> size=3

Answer = 3 (max-set-size) 
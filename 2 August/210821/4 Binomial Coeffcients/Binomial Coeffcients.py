def binomialCoeff(n, r):
    # Implement this function
    # 1.Base case                               			# 1, if r = 0 or n = r
    if(r==0 or n==r):
    	return 1
    
    # 2.Main case
    else:
    	return binomialCoeff(n-1, r-1) + binomialCoeff(n-1, r) #C(n-1, r-1) + C(n-1, r)
# Do not edit anything below
if __name__ == "__main__":
    numTcs = int(input())
    for index in range(numTcs):
        inputInts = input().split(' ')
        n = int(inputInts[0])
        r = int(inputInts[1])
        print(binomialCoeff(n, r))
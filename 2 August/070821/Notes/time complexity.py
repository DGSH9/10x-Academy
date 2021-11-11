#Find min and max
arr = [1,4,-5,88,55]   #--> size of n
def find_min(arr):
    min = 10000
    max = -10000
    for i in range(len(arr)):  # n times
        if(arr[i]<min):
            min=arr[i]    # run as c1 constant time

        if (arr[i]>max):
             max = arr[i] # run as c2 constant time

# calculate Big O notation 
#(c1 * n)  +  (c2 * n)
#O(n) + O(n) => O(2 * n)  =>O(n) time complexity



# Another way but same time complexity
arr = [1,4,-5,88,55]   #--> size of n
def find_min(arr):
    min = 10000
    max = -10000
    for i in range(len(arr)):  # n times
        if(arr[i]<min):
            min=arr[i]    # run as c1 constant time
    
    for j in range(len(arr)):
        if (arr[i]>max):
             max = arr[i] # run as c2 constant time

# calculate Big O notation time complexity
#(c1 * n)  +  (c2 * n)
#O(n) + O(n) => O(2 * n)  =>O(n) time complexity

# Time complexity order =>   O(1) < O(n) < O(n*n)
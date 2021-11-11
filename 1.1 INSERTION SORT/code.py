"""
Insertion Sort
-> Divide in two part  1=>sorted part
                    2=>unsorted part
-> Assume first element is sorted
arr1 = [6,3,9,8,4,5,2]
Sort in Ascending Order



<--------------------PSUDO CODE----------------->

-> First element to be sorted
-> two part exist   =>sorted part and 
                    =>unsorted part
-> In list find correct position of each element on compare with left part

"""
# 8,4,6,3,1,9,5
# 0 1 2 3 4 5 6

def insertionSort(arr1):
    for i in range(1,len(arr1)):
        j = i
        while(j>0 and arr1[j]<arr1[j-1]):
            #swap
            arr1[j],arr1[j-1] =  arr1[j-1],arr1[j]
            #decreament
            j-=1
    return arr1
arr1 = [8,4,6,3,1,9,5]
print(insertionSort(arr1))
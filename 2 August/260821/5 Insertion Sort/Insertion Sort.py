def insertionSort(A, n):
    for i in range(n):
        j=i
        while j>0 and A[j]<A[j-1]:
            A[j],A[j-1] = A[j-1],A[j]
            j-=1
    return A

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*insertionSort(arr, n))
    

# def insertionSort(arr1, n):
#     for i in range(len(arr1)):
#         j=i
#         while j>0 and arr1[j]<arr1[j-1]:
#             arr1[j],arr1[j-1] = arr1[j-1],arr1[j]
#             j-=1
        
#     return arr1

# if __name__ == '__main__':
#     for _ in range(int(input())):
#         n = int(input())
#         arr = [int(x) for x in input().split()]
#         print(*insertionSort(arr, n))

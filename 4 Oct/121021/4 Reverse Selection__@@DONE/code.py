# https://6793fdf6.widgets.sphere-engine.com/lp?hash=rpWDlL2CYG

def reverseSelectionSort(A, n):
    for i in range(n):
        mx_index = i
        for j in range(i+1,n):
            if A[mx_index]<A[j]:
                mx_index = j
        
        A[i],A[mx_index] = A[mx_index],A[i] 
    return A
    

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*reverseSelectionSort(arr, n))
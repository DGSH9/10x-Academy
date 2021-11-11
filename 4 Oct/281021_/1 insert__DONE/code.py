# https://6793fdf6.widgets.sphere-engine.com/lp?hash=4EhUgjNL5A

def insert(arr,n):
    # Your code goes here
    for i in range(len(arr)):
        j = i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    return arr
### DO NOT EDIT ANYTHING BELOW THIS LINE

if __name__=='__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    insert(arr, n)
    print(*arr)
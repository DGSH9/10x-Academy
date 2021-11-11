n = int(input())
if(n>2):
    arr = list(map(int,input().strip().split()))[:n]    
arr.sort()
print(arr[1]-arr[0])
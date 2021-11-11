n = int(input())
arr1 = [int(x) for x in input().split()]

end = 0 
maxlen = 0
len = 1
for i in range(1,n):
    if(arr1[i]>arr1[i-1]):
        len+=1
    else:
        if(len > maxlen):
            maxlen=len
            end = i
        len = 1
if(len > maxlen):
	maxlen = len
	end = n
print(maxlen,end-maxlen+1,end) #length,start,end
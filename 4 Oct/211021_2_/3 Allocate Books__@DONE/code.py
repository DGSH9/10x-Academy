# https://6793fdf6.widgets.sphere-engine.com/lp?hash=hIWWJ1qos7

def students(arr1,mid):
	#mid ->min number of pages max student will get
	pages = 0
	students_count = 1
	
	for i in range(len(arr1)):
		pages +=arr1[i]
		
		if pages > mid:
			pages = arr1[i]
			students_count +=1
	return students_count

def books(arr1,B):
	if B > len(arr1):
		return -1
	left = max(arr1)
	right = sum(arr1)
	
	while(left <= right):
		mid = (left+right)//2
		k = students(arr1,mid)
		if k > B:
			left = mid+1
		else:
			ans = mid
			right = mid-1
	return ans
		
arr1 = [int(x) for x in input().split()]
B = int(input())

print(books(arr1,B))
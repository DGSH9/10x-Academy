# https://6793fdf6.widgets.sphere-engine.com/lp?hash=BJ5Jfhq5rc
# 031021

"""
100->100//5=20
20->20//5  =4     two times
apply binary search



->example dry run==>
 n = 3
 high = 300

"""
def get(num):           #get(150) num = 150,30,6,0
    return1 = 0         #return1 = 0-->30-->30+6=36-->36+0=36
    while(num!=0):      #150->30->6->
        return1+=num//5 
        num = num//5    
    return return1      

for _ in range(int(input())):
    n = int(input())    #n=3
    low = 0             #low = 0     -->
    high = 10**18       #high = 300 -->149
    ans = high          #ans = 300  -->149

    while(low<=high):           #0<100
        mid = (low+high)//2     #mid  =150
        val = get(mid)          #val = get(150) ----->val = 36
        if(val>=n):             #36>=3-->
            high = mid-1        
            ans = min(ans,mid)  
        else:
            low = mid+1
    print(ans)
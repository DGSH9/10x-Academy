# https://6793fdf6.widgets.sphere-engine.com/lp?hash=BkFkLMNKbj

def seating(curr,i,temp,continue_count,res):
    # boundary case
    if i ==temp:
        res.append(curr)
        return
    
    # main case
    if continue_count ==0:
        seating(curr + "a",i+1,temp,1,res)
        seating(curr + "b",i+1,temp,1,res)
    elif(continue_count==1):
        if (curr[-1]=='a'):
            seating(curr + "a",i+1,temp,2,res)
            seating(curr + "b",i+1,temp,1,res)
        else:
            seating(curr + "a",i+1,temp,1,res)
            seating(curr + "b",i+1,temp,2,res)            
    elif(continue_count==2):
        if curr[-1]=="a":
            seating(curr + "b",i+1,temp,1,res)
        else:
            seating(curr + "a",i+1,temp,1,res)


n = int(input())
result = []
seating("",0,n,0,result)
result.sort()

for i in result:
    print(i)
n=input()                      
R_count=0      
G_count=0
for i in range(0,len(n)):
    if(n[i]=="R"):
        R_count+=1
    else:
        G_count+=1    
if(R_count>G_count):
    print(G_count)
else:
    print(R_count)
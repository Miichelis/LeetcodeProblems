def find_s(L,target):
    values=[]
    for i in range(len(L)):
        for j in range(len(L)-1,-1,-1):
            if L[i]+L[j] == target:
                values.append(L[i])
                values.append(L[j])
    if values == []:
        return "no valid parts"
    else:
        return str(values[0])+" "+"and"+" "+str(values[1])
    
            

x=input("Gime me the target num: ")
import random
L=[]
for i in range(10):L.append(random.randint(1,10))
print L
print find_s(L,x)

ls1=list(map(int,(input("listni kiriting\n").split())))
ls2=[]
cnt=ls1.count(0)
for i in ls1:
    if(i!=0):ls2.append(i)
for i in range(cnt):
    ls2.append(0)
print(ls2)
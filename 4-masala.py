n=int(input("nechta tuple kititasiz\n"))

ls=[]
ls2=[]
for i in range(n):
    ls1=list((input("1-listni kiriting\n").split()))
    ls.append(ls1)
for i in range(len(ls)):
   if ls.count(ls[i])==2 and ls2.count(ls[i])==0:ls2.append(ls[i])
print(ls2)
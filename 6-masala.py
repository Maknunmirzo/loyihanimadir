ls1=list((input("1-listni kiriting\n").split()))
ls2=list((input("2-listni kiriting\n").split()))

ln1=len(ls1)
ln2=len(ls2)

minln=min(ln1,ln2)

ls3=[]
 
for i in range(minln):
        ls3.append(ls1[i])
        ls3.append(ls2[i])
      
if len(ls1) > len(ls2):
    ls3.extend(ls1[minln:])
else:
   ls3.extend(ls2[minln:])

print("Natijaviy list",ls3)
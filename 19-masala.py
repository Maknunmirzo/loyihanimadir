ls1=list(map(int,(input("listni kiriting\n").split())))

ls2=list(filter(lambda x:x%2==0,ls1))

ls3=list(filter(lambda x:x%2==1,ls1))

print(ls2)
print(ls3)
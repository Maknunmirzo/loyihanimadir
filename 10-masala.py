n=int(input("sonni kiriyting\n"))

ls=[]

for i in range(n):
    a=int(input("son kiriting\n"))
    ls.append(a)

for i in ls:
    if ls.count(i)<=2:ls.remove(i)
print(ls)
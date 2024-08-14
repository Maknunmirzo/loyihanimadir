def summ(n:int):
    sumn=1
    for i in range(1,n+1):
        sumn*=i
    return sumn
n=int(input("sonni kiriting\n"))
print("natija ",summ(n))
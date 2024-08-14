# def binbin(n:int,sum=0)->int:

#     if(n<2):return sum+n
#     sum=sum*10+n%2
#     return binbin(n//2,sum)

# def teskari(n:int,sum=0):
#     if(n==0):return sum
#     sum=sum*10+n%10
#     return teskari(n//10,sum)

def bimbin(n:int):
    ls=[]
    while(n>1):
        ls.append(n%2)
        n=n//2
    ls.append(n)
    ls.reverse()
    return ls


n=int(input("sonni kiriting\n"))

ls=bimbin(n)

bimm =int("".join(map(str,ls)))

print(bimm)
# print(type(bimm))
ls1 = list(input("1-listni kiriting\n").split())
ls2 = list(input("2-listni kiriting\n").split())

ls3 = []

for i in ls1:
    if ls2:
        j = ls2.pop(0)  # ls2 dan birinchi elementni olamiz va o'chiramiz
        ls3.append(i)
        ls3.append(j)
        
print("Natijaviy list:", ls3)

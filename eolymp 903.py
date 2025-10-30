a = input()
lst = []
a1 , a2 = int(a[0]) , int(a[2])
lst.append(a1)
lst.append(a2)
if a1 == a2:
    print("=")
elif a1 > a2:
    print(a1)
else:
    print(a2)
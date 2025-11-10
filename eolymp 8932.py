a = input().split()
s=[]
a1 , a2 = int(a[0]), int(a[1])
a.sort()
for i in range(a1 , a2 +1):
    s.append(str(i))
print(" ".join(s))
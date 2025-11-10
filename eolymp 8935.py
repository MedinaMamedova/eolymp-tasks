a = input().split()
a1 , a2 = int(a[0]), int(a[1])
s = []
for i in range (a1 , a2+1):
    if i % 2 == 1:
        s.append(str(i))
print(" ".join(s))
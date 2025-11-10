a = input().split()
a = list(map(lambda x: int(x), a))
a.sort()
a1 , a2 , a3 = a[0] , a[1] , a[2]
if a1**2 + a2**2 == a3**2:
    print("YES")
else:
    print("NO")
sides = input().split()
a1, a2, a3, a4 = sides[0], sides[1],sides[2],sides[3]
if a1 == a2 and a3 == a4:
    print("YES")
elif a1 == a3 and a2 == a4:
    print("YES")
elif a1 == a4 and a3 == a2:
    print("YES")
else:
    print("NO")

sides = input().split()
a1 , a2 , a3 = int(sides[0]), int(sides[1]), int(sides[2])
if a1 == a2 == a3:
    print("1")
elif a1 == a2 != a3 or a1 == a3 != a2 or a2 == a3 != a1:
    print("2")
else:
    print("3")
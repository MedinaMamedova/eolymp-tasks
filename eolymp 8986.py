a = input()
b = input().split()
b1 , b2 = int(b[0]), int(b[1])
print(a[:b1] + a[b2+1:])
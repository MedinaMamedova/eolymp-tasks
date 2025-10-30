numbers = input().split()
a1, a2, a3 = int(numbers[0]), int(numbers[1]), int(numbers[2])
discr = a2**2 - 4*a1*a3
roots=[]
if discr == 0:
    k1 = (-a2)/2*a1
    print(int(k1)) 
elif discr > 0:
    k1 = (-a2-(discr)**0.5)/(2*a1)
    k2 = (-a2+(discr)**0.5)/(2*a1)
    roots.append(k1)
    roots.append(k2)
    print(roots.sort())
else:
     print("No roots")
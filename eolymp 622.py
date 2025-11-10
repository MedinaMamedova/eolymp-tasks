a = int(input())
s = ""
while a >= 1:
    k = a % 2 
    a = a // 2
    s = s + str(k)
print(s.count("1"))
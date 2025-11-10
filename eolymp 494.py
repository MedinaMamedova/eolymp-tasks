a = input()
a = a.upper()
s = 0
for i in a:
    if i in "AIUOEY":
        s = s + 1
print(s)
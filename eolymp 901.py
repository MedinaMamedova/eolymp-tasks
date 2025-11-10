a = input()
b = a. count ("+") + a.count("*") +a.count("-") 
if a[0] in "-+":
    b = b - 1
print(b)
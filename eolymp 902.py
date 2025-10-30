score =int(input())
if 1 <= score <= 3:
    print("Inital")
elif 4 <= score <= 6:
    print("Average")
elif 7 <= score <= 9:
    print("Sufficient")
else:
    print("High")
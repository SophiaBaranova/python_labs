a = input("enter string: ")
if len(a) < 4:
    print("the string is too short to slice")
else:
    print("the string from the second symbol from the start to the second symbol from the end (the second symbol from the end is included):")
    print(a[1:-1])

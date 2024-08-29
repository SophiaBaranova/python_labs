a = input("enter string: ")
print("ascii code of the string:")
for x in a:
    if x.isalpha():
        print(ord(x), end=" ")
    else:
        print(x, end=" ")
print()

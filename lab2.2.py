from mod import isDeficient

n = int(input("enter n to check if it is deficient: "))
if isDeficient(n):
    print(f"{n} is deficient")
else:
    print(f"{n} is not deficient")

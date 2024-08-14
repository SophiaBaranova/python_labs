n = int(input("enter n (integer in range 1-9): "))
while (n < 1 or n > 9):
    n = int(input("enter a valid value: "))
for i in range(-n, n + 1):
    if i == 0:
        continue
    print(" "*(n-abs(i)-1), f"{n}"*(abs(i)-1))
print("finish")

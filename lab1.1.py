a = int(input("enter a (integer in range 1-100): "))
while(a < 1 or a > 100):
    a = int(input("enter a valid value: "))
b = int(input("enter b (integer in range 1-100): "))
while(b < 1 or b > 100):
    b = int(input("enter a valid value: "))
if a > b:
    X = b * a + 1
elif a == b:
    X = 3425
else:
    X = (2 * a - 5) / b
print(f"X = {X:.2f}")
print("finish")
a = input("enter string: ")
s = ["i", "a", "o"]
flag = 0
for x in s:
    if x in a:
        print(f"there are {a.count(x)} substitution(s) of cyrillic symbol '{x}' to latin")
        flag = 1
if not flag:
    print("there are no substitutions of cyrillic symbols 'i', 'a', 'o' to latin")

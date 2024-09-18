def intersect():
    #введення множин А і В
    A = set(map(int, input("enter A - set of integers: ").split()))
    B = set(map(int, input("enter B - set of integers: ").split()))
    #знаходження перетину А і В
    C = A & B
    #виведення множин
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = A & B = {C}")

intersect()

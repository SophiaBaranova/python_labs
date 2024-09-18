def float_to_int():
    #введення списку з дійсних чисел
    A = list(map(float, input("enter a list of floats: ").split()))
    #округлення елементів до цілого
    B = list(map(round, A))
    #виведення списків
    print(f"initial list: {A}")
    print(f"list after rounding the elements to integers: {B}")

float_to_int()

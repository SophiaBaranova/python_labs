#введення розміру масиву
n = int(input("enter size of the array: "))
print("enter elements of the array: ")
#введення елементів
arr = [int(input(f"array[{i}] -> ")) for i in range(n)]
#виведення оригінального масиву
print(f"original array: {arr}")
#перестановка елементів у зворотньому порядку
arr.reverse()
#виведення модифікованого масиву
print(f"reversed array: {arr}")


import re

def shortest_word():
    #введення рядка
    A = input("enter a list of words: ")
    #видалення з рядка пунктуаційних та інших зайвих символів
    A = re.sub(r'[^a-zA-Z\s\']', '', A)
    #перетворення рядка на список
    A = A.split()
    #пошук найкоротшого слова у списку
    shortest = A[0]
    for a in A:
        if len(shortest) > len(a):
            shortest = a
    #виведення списку
    print(f"list: {A}")
    #виведення найкоротшого слова
    print(f"the shortest word in the list: {shortest}")

shortest_word()


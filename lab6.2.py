import re

def shortest_word():
    #�������� �����
    A = input("enter a list of words: ")
    #��������� � ����� ������������� �� ����� ������ �������
    A = re.sub(r'[^a-zA-Z\s\']', '', A)
    #������������ ����� �� ������
    A = A.split()
    #����� ������������ ����� � ������
    shortest = A[0]
    for a in A:
        if len(shortest) > len(a):
            shortest = a
    #��������� ������
    print(f"list: {A}")
    #��������� ������������ �����
    print(f"the shortest word in the list: {shortest}")

shortest_word()


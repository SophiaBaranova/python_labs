def intersect():
    #�������� ������ � � �
    A = set(map(int, input("enter A - set of integers: ").split()))
    B = set(map(int, input("enter B - set of integers: ").split()))
    #����������� �������� � � �
    C = A & B
    #��������� ������
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = A & B = {C}")

intersect()

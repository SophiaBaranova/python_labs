def float_to_int():
    #�������� ������ � ������ �����
    A = list(map(float, input("enter a list of floats: ").split()))
    #���������� �������� �� ������
    B = list(map(round, A))
    #��������� ������
    print(f"initial list: {A}")
    print(f"list after rounding the elements to integers: {B}")

float_to_int()

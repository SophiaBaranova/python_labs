#�������� ������ ������
n = int(input("enter size of the array: "))
print("enter elements of the array: ")
#�������� ��������
arr = [int(input(f"array[{i}] -> ")) for i in range(n)]
#��������� ������������ ������
print(f"original array: {arr}")
#������������ �������� � ����������� �������
arr.reverse()
#��������� �������������� ������
print(f"reversed array: {arr}")


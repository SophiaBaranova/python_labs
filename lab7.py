def main():
    #��������� �������� - �������� ������ �� ������� ����
    trains_sumy = {143: {"�����������": ["�����-���������", "����"], "��������": [9, 56], "�����������": "-"}, 280: {"�����������": ["���", "����"], "��������": [13, 19], "�����������": "-"}, 780: {"�����������": ["���", "����"], "��������": [21, 43], "�����������": "-"}, 114: {"�����������": ["����", "�����"], "��������": [15, 50], "�����������": [16, 10]}, 144: {"�����������": ["�����", "����"], "��������": [10, 0], "�����������": "-"}, 279: {"�����������": ["����", "���"], "��������": "-", "�����������": [14, 50]}, 779: {"�����������": ["����", "���"], "��������": "-", "�����������": [6, 43]}, 45: {"�����������": ["�������", "�����"], "��������": [8, 49], "�����������": [9, 9]}, 113: {"�����������": ["�����", "����"], "��������": [1, 18], "�����������": [1, 38]}}
    print("� ������ ������������ ������� ������ �� ������� ����. �� ������ �������?")
    print("1 - ������ ���������� ��� ����� �����\n2 - �������� ���������� ��� �����\n3 - ����������� �������\n4 - ����������� �������, ������������ �� �������� ������\n5 - ���������, �� ������ ����������� �� ������� � ������ ������ ����")
    go = "���"
    while go == "���":
        #����� ��������
        try:
            oper = int(input("�������� -> "))
        except ValueError:
            print("������� ��������")
            go = input("������ ����������? (���/�) -> ")
            continue
        #��������� ��������
        if oper == 1:
            trains_sumy = add_train(trains_sumy)
        elif oper == 2:
            trains_sumy = del_train(trains_sumy)
        elif oper == 3:
            print_trains(trains_sumy)
        elif oper == 4:
            print_trains_sorted(trains_sumy)
        elif oper == 5:
            search_train(trains_sumy)
        else:
            print("������� ��������")
        go = input("������ ����������? (���/�) -> ")
    print("������� ��� :)")

#��������� ���������� ��� ����� �����
def add_train(trains_sumy):
    err = 1
    while err == 1:
        #�������� ������
        try:
            number = int(input("����� -> "))
        except ValueError:
            print("��������� ���")
        else:
            err = 0
    #���� ����� ��� � � �������
    if number in trains_sumy:
        go = input("����� ��� � � �������, ������ ���? (���/�) -> ")
        if go == "�":
            return trains_sumy
    err = 1
    while err == 1:
        #�������� �����������
        a = list(input("����������� (����� �����) -> ").split())
        if len(a) != 2:
            print("��������� ���")
        else:
            err = 0
    #���� ��������� ������� - ����
    if a[0] == "����":
            #������� ��� ��������
            b = "-"
    else:
        err = 1
        while err == 1:
            #�������� ���� ��������
            try:
                b = list(map(int, input("��� �������� (����� ����� ��� � ��) -> ").split()))
            except ValueError:
                print("��������� ���")
            else:
                if len(b) != 2 or (b[0] < 0 or b[0] > 23) or (b[1] < 0 or b[1] > 59):
                    print("��������� ���")
                else:
                    err = 0
    #���� ������ ������� - ����
    if a[1] == "����":
            #������� ��� �����������
            c = "-"
    else:
        err = 1
        while err == 1:
            #�������� ���� �����������
            try:
                c = list(map(int, input("��� ����������� (����� ����� ��� � ��) -> ").split()))
            except ValueError:
                print("��������� ���")
            else:
                if len(c) != 2 or (c[0] < 0 or c[0] > 23) or (c[1] < 0 or c[1] > 59):
                    print("��������� ���")
                else:
                    err = 0
    #��������� �������� �� ������ ��� ����� �����
    new_train = dict(����������� = a, �������� = b, ����������� = c)
    #��������� ������ ������ �� ��������
    trains_sumy[number] = new_train
    print("����� ������ ������ �� ��������")
    return trains_sumy

#��������� ���������� ��� �����
def del_train(trains_sumy):
    err = 1
    while err == 1:
        #�������� ������ ������
        try:
            number = int(input("����� -> "))
        except ValueError:
            print("��������� ���")
        else:
            err = 0
    #��������� ������ �� ��������
    try:
        trains_sumy.pop(number)
    except KeyError:
        print("����� ������� � �������")
    else:
        print("����� ������ �������� � ��������")
    return trains_sumy

#��������� ��������
def print_trains(trains_sumy):
    for train in trains_sumy:
        print(f"{train}: {trains_sumy[train]["�����������"]}, �������� {trains_sumy[train]["��������"]}, ����������� {trains_sumy[train]["�����������"]}")

#��������� ��������, ������������� �� �������� ������
def print_trains_sorted(trains_sumy):
    #���������� �������� �� ������� - �������� ������
    trains_sumy = {k: trains_sumy[k] for k in sorted(trains_sumy)}
    #��������� ��������
    for train in trains_sumy:
        print(f"{train}: {trains_sumy[train]["�����������"]}, �������� {trains_sumy[train]["��������"]}, ����������� {trains_sumy[train]["�����������"]}")

#����� ������, �� ����������� �� ������� ���� � ������ ������ ����
def search_train(trains_sumy):
    err = 1
    while err == 1:
        #�������� ����
        try:
            time = list(map(int, input("��� (����� ����� ��� � ��) -> ").split()))
        except ValueError:
            print("��������� ���")
        else:
            if (time[0] < 0 or time[0] > 23) or (time[1] < 0 or time[1] > 59):
                print("��������� ���")
            else:
                err = 0
    count = 0
    #����� ������
    for train in trains_sumy:
        #���� ���� - ��������� ��� ������ �������
        if trains_sumy[train]["��������"] == "-" or trains_sumy[train]["�����������"] == "-":
            if trains_sumy[train]["��������"] == "-":
                diff = list(map(lambda x, y: x - y, trains_sumy[train]["�����������"], time))
            else:
                diff = list(map(lambda x, y: x - y, time, trains_sumy[train]["��������"]))
            diff_min = diff[0] * 60 + diff[1]
            #���� ������ �� ����� ��������/����������� � ������� ����� "��'����" ��� ����� 20 ��
            if diff_min > 20 or diff_min < 0:
                continue
        else:
            diff = list(map(lambda x, y: x - y, time, trains_sumy[train]["��������"]))
            #���� ����� ������� �����
            if diff[0] < 0 or (diff[0] < 1 and diff[1] < 0):
                continue
            #���� ����� ������������� �����
            diff = list(map(lambda x, y: x - y, trains_sumy[train]["�����������"], time))
            if diff[0] < 0 or (diff[0] < 1 and diff[1] < 0):
                continue
        #��������� ���������� ��� �����
        print(f"{train}: {trains_sumy[train]["�����������"]}, �������� {trains_sumy[train]["��������"]}, ����������� {trains_sumy[train]["�����������"]}")
        count += 1
    if count == 0:
        print("�� ������� ��� ������ ������")

#������ main() ������� ��������
if __name__ == '__main__':
    main()

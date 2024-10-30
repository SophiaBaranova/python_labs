import json

def main():
    #відкриття файлу з вхідними даними
    try:
        inFile = open("trains.json", "r")
    except:
        print("неможливо відкрити файл із вхідними даними")
        return
    #завантаження вмісту файлу до словника
    trains_sumy = json.load(inFile)
    #закриття файлу
    inFile.close()
    print("У Вашому розпорядженні розклад потягів по станції Суми. Що бажаєте зробити?")
    print("1 - додати інформацію про новий потяг\n2 - видалити інформацію про потяг\n3 - переглянути розклад\n4 - визначити, які потяги перебувають на станції у певний момент часу")
    go = "так"
    while go == "так":
        #запит операції
        try:
            oper = int(input("операція -> "))
        except ValueError:
            print("невідома операція")
            go = input("Бажаєте продовжити? (так/ні) -> ")
            continue
        #виконання операції
        if oper == 1:
            trains_sumy = add_train(trains_sumy)
        elif oper == 2:
            trains_sumy = del_train(trains_sumy)
        elif oper == 3:
            print_trains(trains_sumy)
        elif oper == 4:
            search_train(trains_sumy)
        else:
            print("невідома операція")
        go = input("Бажаєте продовжити? (так/ні) -> ")
    #перетворення словника у формат json
    trains_sumy = json.dumps(trains_sumy, ensure_ascii = False)
    #відкриття файлу для запису
    try:
        outFile = open("new_trains.json", "w")
    except:
        print("неможливо створити файл для запису результатів")
        return
    #запис оновлених даних у файл
    outFile.write(trains_sumy)
    #закриття файлу
    outFile.close()
    print("Гарного дня :)")

#додавання інформації про новий потяг
def add_train(trains_sumy):
    err = 1
    while err == 1:
        #введення номера
        try:
            number = int(input("номер -> "))
        except ValueError:
            print("некоректні дані")
        else:
            err = 0
    number = str(number)
    #якщо потяг вже є у розкладі
    if number in trains_sumy:
        go = input("потяг вже є у розкладі, змінити дані? (так/ні) -> ")
        if go == "ні":
            return trains_sumy
    err = 1
    while err == 1:
        #введення призначення
        a = list(input("призначення (через пробіл) -> ").split())
        if len(a) != 2:
            print("некоректні дані")
        else:
            err = 0
    #якщо початкова станція - Суми
    if a[0] == "Суми":
            #відсутній час прибуття
            b = "-"
    else:
        err = 1
        while err == 1:
            #введення часу прибуття
            try:
                b = list(map(int, input("час прибуття (через пробіл год і хв) -> ").split()))
            except ValueError:
                print("некоректні дані")
            else:
                if len(b) != 2 or (b[0] < 0 or b[0] > 23) or (b[1] < 0 or b[1] > 59):
                    print("некоректні дані")
                else:
                    err = 0
    #якщо кінцева станція - Суми
    if a[1] == "Суми":
            #відсутній час відправлення
            c = "-"
    else:
        err = 1
        while err == 1:
            #введення часу відправлення
            try:
                c = list(map(int, input("час відправлення (через пробіл год і хв) -> ").split()))
            except ValueError:
                print("некоректні дані")
            else:
                if len(c) != 2 or (c[0] < 0 or c[0] > 23) or (c[1] < 0 or c[1] > 59):
                    print("некоректні дані")
                else:
                    err = 0
    #створення словника із даними про новий потяг
    new_train = dict(призначення = a, прибуття = b, відправлення = c)
    #додавання нового потяга до розкладу
    trains_sumy[number] = new_train
    print("потяг успішно додано до розкладу")
    return trains_sumy

#видалення інформації про потяг
def del_train(trains_sumy):
    err = 1
    while err == 1:
        #введення номеру потяга
        try:
            number = int(input("номер -> "))
        except ValueError:
            print("некоректні дані")
        else:
            err = 0
    number = str(number)
    #видалення потяга із розкладу
    try:
        trains_sumy.pop(number)
    except KeyError:
        print("потяг відсутній у розкладі")
    else:
        print("потяг успішно видалено з розкладу")
    return trains_sumy

#виведення розкладу
def print_trains(trains_sumy):
    for train in trains_sumy:
        print(f"{train}: {trains_sumy[train]["призначення"]}, прибуття {trains_sumy[train]["прибуття"]}, відправлення {trains_sumy[train]["відправлення"]}")

#пошук потягів, що перебувають на станції Суми у певний момент часу
def search_train(trains_sumy):
    err = 1
    while err == 1:
        #введення часу
        try:
            time = list(map(int, input("час (через пробіл год і хв) -> ").split()))
        except ValueError:
            print("некоректні дані")
        else:
            if (time[0] < 0 or time[0] > 23) or (time[1] < 0 or time[1] > 59):
                print("некоректні дані")
            else:
                err = 0
    count = 0
    #пошук потягів
    for train in trains_sumy:
        #якщо Суми - початкова або кінцева станція
        if trains_sumy[train]["прибуття"] == "-" or trains_sumy[train]["відправлення"] == "-":
            if trains_sumy[train]["прибуття"] == "-":
                diff = list(map(lambda x, y: x - y, trains_sumy[train]["відправлення"], time))
            else:
                diff = list(map(lambda x, y: x - y, time, trains_sumy[train]["прибуття"]))
            diff_min = diff[0] * 60 + diff[1]
            #якщо різниця між часом прибуття/відправлення і заданим часом "від'ємна" або більше 20 хв
            if diff_min > 20 or diff_min < 0:
                continue
        else:
            diff = list(map(lambda x, y: x - y, time, trains_sumy[train]["прибуття"]))
            #якщо потяг прибуває пізніше
            if diff[0] < 0 or (diff[0] < 1 and diff[1] < 0):
                continue
            #якщо потяг відправляється пізніше
            diff = list(map(lambda x, y: x - y, trains_sumy[train]["відправлення"], time))
            if diff[0] < 0 or (diff[0] < 1 and diff[1] < 0):
                continue
        #виведення інформації про потяг
        print(f"{train}: {trains_sumy[train]["призначення"]}, прибуття {trains_sumy[train]["прибуття"]}, відправлення {trains_sumy[train]["відправлення"]}")
        count += 1
    if count == 0:
        print("на заданий час потяги відсутні")

#виклик main() функції програми
if __name__ == '__main__':
    main()


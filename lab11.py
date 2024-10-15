import csv

#відкриття файлу з вхідними даними
try:
    input_f = open("input.csv", "r")
except:
    #помилка відкриття
    print("input file couldn't be opened")
else:
    #читання з файлу
    reader = csv.DictReader(input_f, delimiter = ",")
    print("Exports of goods and services (% of GDP)")
    print("%30s %6d %6d" % ("Country", 2015, 2016))
    #виведення даних
    for row in reader:
        print("%30s" % row['Country Name'], end = " ")
        try:
            print("%6.2f" % float(row['2015 [YR2015]']), end = " ")
        except:
            #числові дані відсутні
            print("%6s" % "-", end = " ")
        try:
            print("%6.2f" % float(row['2019 [YR2019]']))
        except:
            #числові дані відсутні
            print("%6s" % "-")
    #перехід на початок файлу
    input_f.seek(0)
    #читання з файлу
    reader = csv.DictReader(input_f, delimiter = ",")
    #відкриття файлу для запису результатів
    try:
        output_f = open("output.csv", "w")
    except:
        #помилка відкриття
        print("output file couldn't be opened")
    else:
        #введення діапазону для пошуку
        while True:
            try:
                val = list(map(float, input("search range -> ").split()))
            except:
                print("invalid range")
            else:
                break
        #введення року для пошуку
        while True:
            year = input("year: ")
            if year != '2015' and year != '2019':
                print("invalid year")
            else:
                break
        #запис у файл
        writer = csv.DictWriter(output_f, fieldnames = ['Country Name', year], delimiter = ",")
        #запис заголовків у файл
        writer.writeheader()
        #пошук потрібних значень
        for row in reader:
            try:
                if year == '2015':
                    r = float(row['2015 [YR2015]'])
                else:
                    r = float(row['2019 [YR2019]'])
            #числові дані відсутні
            except:
                continue
            #значення належить потрібному діапазону
            if r > val[0] and r < val[1]:
                #виведення даних
                print("%30s %6.2f" % (row['Country Name'], r))
                #запис даних у файл
                writer.writerow({'Country Name': row['Country Name'], year: r})
        #закриття файлу з результатами
        output_f.close()
    #закриття файлу з вхідними даними
    input_f.close()

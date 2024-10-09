#функція для відкриття файлу
def open_file(file_name, mode):
    try:
        p = open(file_name, mode)
    except:
        print(f"file {file_name} couldn't be opened")
        return None
    return p

#функція для заміни в рядку 1 на 0 і навпаки
def modify(str, s1, s2):
    temp = ""
    for symbol in str:
        if symbol == s1:
            symbol = s2
        elif symbol == s2:
            symbol = s1
        temp += symbol
    return temp

def main():
    #вихіний текст
    text = "In the second quarter of 2019, retail sales in Canada reached $163.3 billion, up 1.4% from the same quarter of 2018. Sales were up in 13 of 19 commodity groupings for the second quarter of 2019.\nThe largest increase in dollar terms came from food, which posted a year-over-year growth of 3.5%.\nThe majority of this gain was attributable to higher sales of fresh food (+3.4%), led by growth in sales of fresh fruit and vegetables (+5.4%). Sales of packaged food dry goods increased 4.4%, while sales of frozen food grew 1.1%."
    #довжина рядка для запису в TF23_2
    n = 15
    #кількість повних рядків для запису в TF23_2
    m = len(text) // n
    #відкриття файлів
    p1 = open_file("TF23_1", "w+")
    p2 = open_file("TF23_2", "w+")
    #якщо файли вдалося відкрити
    if p1 != None and p2 != None:
        #запис тексту в TF23_1
        p1.write(text)
        #встановлення вказівника на початок TF23_1
        p1.seek(0)
        for i in range(m):
            #зчитування n символів з TF23_1
            temp = p1.read(n)
            #заміна 1 на 0 і навпаки
            temp = modify(temp, "1", "0")
            #запис рядка в TF23_2
            p2.write(temp + "\n")
        #зчитування тексту, що залишився в TF23_1
        temp = p1.read()
        #заміна 1 на 0 і навпаки
        temp = modify(temp, "1", "0")
        #запис тексту, що залишився, в TF23_2
        p2.write(temp)
        #встановлення вказівника на початок TF23_2
        p2.seek(0)
        #порядкове виведення вмісту TF23_2
        for line in p2:
            print(line, end = "")
        print()
    #закриття файлів
    p1.close()
    p2.close()

#виклик main() функції програми
if __name__ == '__main__':
    main()



# Импорт библиотек
import csv

with open('rocket.csv', encoding="utf-8") as csvfile: # Чтение файла
    reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
    my_dict = {}
    name_month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    for el in reader:
        data = int((el['date'].split('-')[1])) - 1
        if name_month[data] not in my_dict:
            my_dict[name_month[data]] = 1
        else:
            my_dict[name_month[data]] += 1


your_answer = input()
for row in reader:
    if (row['date'].split('-'))[1] == your_answer:
        print(f'В {your_answer} было получено - {my_dict[your_answer]} шифров')
        break


with open('rocket_part.txt', 'w', encoding="utf-8") as file: # Запись данных в новый файл
    names = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    for i in range(len(names)):
        file.write(f'В {names[i]} было получено - {my_dict[names[i]]} шифров\n')
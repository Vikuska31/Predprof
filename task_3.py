# Импорт библиотек
import csv

with open('rocket.csv', encoding="utf-8") as csvfile:
    reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))

#Поиск данных в файле
your_data = input()
while your_data != 'sleep':
    for row in reader:
        if  your_data == row['date']:
            print(f"Шифр: <{row['code']} от: {row['rocketparts']} был получен {row['date']}")
            break 
        else:
            print('в этот день космос молчал')
            break
    your_data = input()
    if your_data == 'sleep':
        break
    your_data = input()

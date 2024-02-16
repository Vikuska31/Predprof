def sorting(el):
    '''
    Функция для сортироки массива
    el - список данных
    return: отсортированный по убыванию список
    '''
    for i in range(len(el)):
        j = i - 1
        key = el[i]
        while int(el[j]) < int(key) and j >= 0:
            el[j + 1] = el[j]
            j -= 1
        el[j + 1] = key
    return el

with open('rocket_part.txt', encoding="utf-8") as file:
    mas = file.readlines()
    new_mas = []
    for i in range(len(mas)):
        el = mas[i].split()[-2]
        new_mas.append(el)
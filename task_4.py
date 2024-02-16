# Импорт библиотек
import csv
import random

   
rus_alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
eng_alph = ''.join(sorted('QWERTYUIOPASDFGHJKLZXCVBNM'))

def create_code(s: str) -> str:
    '''
    Функция для создания кода
    s - исходный код
    return: исправленный код
    '''
    digits = ''
    rus_simb = ''
    eng_simb = ''
    for i in s:
        if i in '0123456789':
            digits += i
        if i in rus_alph:
            rus_simb += i
        if i in eng_alph:
            eng_simb += i
    return digits + eng_simb + rus_simb

with open('rocket.csv', encoding="utf-8") as csvfile:
    reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))

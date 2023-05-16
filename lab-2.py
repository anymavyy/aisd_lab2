# Вариант 15.
# Натуральные числа, расположенные в порядке возрастания.
# Для каждой такой последовательности минимальное число вывести прописью.
import re

dict = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
        9: 'девять'}
min_num = "0"
count = 0
check = 0
file = open("input.txt", "r")
marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''
while True:
    a = file.readline().split()
    if not a:
        print('\nКонец файла')
        break
    print("Числа:", end=' ')
    for j in a:
        for x in j:
            if x in marks:
                j = j.replace(x, "")  # убираем лишние знаки
        res = re.findall(r'[0-9]?[0-9]?[0-9]{1}', j)  # ищем число по условию
        if len(res) == 1:
            if len(j) == len(res[0]) and len(j) > 0:
                count += 1
                if int(res[0]) > int(min_num):
                    if check == 0:
                        min_num = res[0]
                        for j in range(len(min_num)):
                            for l in dict:
                                if str(l) == min_num[j]:
                                    print(dict[l], end=' ')
                                    break
                        print('', end='|')
                        check += 1
                    else:
                        min_num = res[0]
                elif int(res[0]) < int(min_num):
                    min_num = res[0]
                    for j in range(len(min_num)):
                        for l in dict:
                            if str(l) == min_num[j]:
                                print(dict[l], end=' ')
                                break
                    print('', end='|')
if check == 0:
    print('В файле нет чисел, удовлетворяющих условию')

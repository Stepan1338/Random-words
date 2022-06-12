import random
import sys
count = sum(1 for line in open('word_list.txt', 'r', encoding='utf8')) #открытие файла
print('Количество строк в словаре:', count)
num = input('Введите число повторений цикла: ')
num = int(num)
print('Выводится строка, вы нажимаете на enter и получаете новое слово.' )
print('Чтобы выйти из заданного вами цикла нужно ввести английскую q')


f = open('word_list.txt', 'r', encoding='utf8')

data = f.read()
lines = data.split('\n')
#print(lines)
used_words = []
i = num
j = 0
for line in range(i):
    try:
        line = random.choice(lines)
    except IndexError:
        print('Не осталось выбора в списке, слова закончились!')
        break
    if line in used_words:
        num = num + 1
    else:
        used_words = used_words + list(line)
        print(line)
        lines.remove(line)
    i = num
    j = j + 1
    #print(j)

    w = input()
    if w == 'q':
        break

f.close()
print('Цикл закончен, файл закрыт')
end = input('Нажмите ENTER для закрытия программы')
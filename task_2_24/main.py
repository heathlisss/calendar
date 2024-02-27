# ---------------------------------------------------------------------------------------------------------------------
# Реализовать функцию, которая будет возвращать двумерный массив целых чисел в виде календаря на заданный месяц.
# Функция должна принимать два числа – номер и номер года, например:
# (11, 2017)	→
# 30, 31, 1,  2,  3,  4,  5
# 6,  7,  8,  9,  10, 11, 12
# 13, 14, 15, 16, 17, 18, 19
# 20, 21, 22, 23, 24, 25, 26
# 27, 28, 29, 30, 1,   2,  3
# ---------------------------------------------------------------------------------------------------------------------

def write_calendar_to_file(previous_month, current_month):
    with open('calendar.txt', 'w') as file:
        count = 0
        for i in range(previous_month - denNed + 1, previous_month + 1):
            file.write(str(i) + ' ')
            count += 1
        for i in range(1, current_month + 1):
            file.write(str(i) + ' ')
            if i < 10 :
                file.write(' ')
            count += 1
            if count == 7:
                file.write('\n')
                count = 0
        if count != 0:
            for i in range(1, 7 - count + 1):
                file.write(str(i) + ' ')
                if i < 10:
                    file.write(' ')


def read_lists_from_file(file_name):
    with open(file_name, 'r') as file:  # открывает файл только для чтения('r')
        lines = file.readlines()
        list1 = [int(num) for num in lines[0].split()]  # проходит по числам строки и записывает их в список
    return list1


mon, god = read_lists_from_file('test.txt')

# код месяца
m = int({
            1 or 10: 1,
            5: 2,
            8: 3,
            2 or 3 or 11: 4,
            6: 5,
            12 or 9: 6,
            4 or 7: 0
        }.get(mon, None))

# код года
kof = int({
              3: 0,
              2: 2,
              1: 4,
              0: 6
          }.get(god // 100 % 4, None))

g = (kof + god % 100 + god % 100 // 4) % 7

# код первого дня в месяце
d = (1 + m + g) % 7
if d == 0:
    denNed = 5
elif d == 1:
    denNed = 6
else:
    denNed = d - 2

f = 0
if ((god % 4 == 0 and god % 100 != 0) or god % 400 == 0):
    f = 1
    if mon < 3:
        if denNed > 0:
            denNed -= 1
        else:
            denNed = 6
print(denNed)
# печать
if mon == (1 or 8):
    write_calendar_to_file(31, 31)
elif mon == (10 or 5 or 12 or 7):
    write_calendar_to_file(30, 31)
elif mon == 3:
    if (f == 1):
        write_calendar_to_file(29, 31)
    else:
        write_calendar_to_file(28, 31)
elif mon == 2:
    if (f == 1):
        write_calendar_to_file(31, 29)
    else:
        write_calendar_to_file(31, 28)
else:
    write_calendar_to_file(31, 30)

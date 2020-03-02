from Compare import Color
import pyperclip
import re

with open('new.xml', 'r', encoding='UTF8') as file:
    new = file.read()

with open('old.xml', 'r', encoding='UTF8') as file:
    old = file.read()

# ----------- Фильтрация новой, оставляем только "Идентификатор происшествия" ------------------
scanNew = r'ID > .*[1234567890]'
tempNew = re.findall(scanNew, new)

new_Stat = []  # x

for i in tempNew:
    new_Stat.append("{}".format(i[5:]))


# ----------- Фильтрация старой ......------------------
scanOld = r'ID > .*[1234567890]'
tempOld = re.findall(scanOld, old)

old_Stat = []  # x

for i in tempOld:
    old_Stat.append("{}".format(i[5:]))

# ------ Фильтрация обоих закончена -------------------------------------------------------------


Color.green('+++ Лишние в новой +++')
for x in set(new_Stat).difference(old_Stat):
    Color.green(x)


Color.red('+++ Лишние в старой +++')
for z in set(old_Stat).difference(new_Stat):
    Color.red(z)


Color.green('\n' + ' ### Повторы в новой ###')
new_double = []
for x in new_Stat:
    if new_Stat.count(x) > 1:
        new_double.append(x)
        new_double.sort()

for x in new_double:
    Color.green(x)


Color.red('### Повторы в старой ###')
old_double = []
for z in old_Stat:
    if old_Stat.count(z) > 1:
        old_double.append(z)
        old_double.sort()

for z in old_double:
    Color.red(z)




# new = True
# old = True
#
# Color.green('------- new_Stat -------------------------------')
#
# for x in new_Stat:  # выводит лишние поля из новой
#     zEnd = 0
#
#     for z in old_Stat:
#         zEnd = zEnd + 1
#         if x == z:
#             break
#         if x != z and zEnd == len(old_Stat):
#             Color.yellow(x)
#             new = False
#
# Color.red('------- old_Stat -------------------------------' + '\n')
#
# for z in old_Stat:  # выводит лишние поля из старой
#     xEnd = 0
#
#     for x in new_Stat:
#         xEnd = xEnd + 1
#         if x == z:
#             break
#         if x != z and xEnd == len(new_Stat):
#             Color.red(z)
#             old = False
#
# if new is True and old is True:
#     Color.green("Все поля совпали")

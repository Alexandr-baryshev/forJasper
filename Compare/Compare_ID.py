from Compare import xml_new
from Compare import Color

import pyperclip

new_Stat = [11, 2, 88, 4, 88, 11, 88]  # x
new_double = []

old_Stat = [1, 2, 3, 5, 2]  # z
old_double = []


Color.green('------- Лишние в новой ------------------')
for x in set(new_Stat).difference(old_Stat):
    Color.green(x)


Color.red('------- Лишние в старой ------------------')
for z in set(old_Stat).difference(new_Stat):
    Color.red(z)


Color.white('------- Повторы в новой ------------------')
for x in new_Stat:
    if new_Stat.count(x) > 1:
        new_double.append(x)
        new_double.sort()

for x in new_double:
    Color.green(x)

Color.white('------- Повторы в старой ------------------')
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

from Compare import xml_new
from Compare import Color

import pyperclip

new_Stat = [1, 2, 3, ]  # x
new_notFinde = []

old_Stat = [1, 2, 3, ]  # z

new = True
old = True

Color.green('------- new_Stat -------------------------------')

for x in new_Stat:  # выводит лишние поля из новой
    zEnd = 0

    for z in old_Stat:
        zEnd = zEnd + 1
        if x == z:
            break
        if x != z and zEnd == len(old_Stat):
            Color.yellow(x)
            new = False

Color.red('------- old_Stat -------------------------------' + '\n')

for z in old_Stat:  # выводит лишние поля из старой
    xEnd = 0

    for x in new_Stat:
        xEnd = xEnd + 1
        if x == z:
            break
        if x != z and xEnd == len(new_Stat):
            Color.red(z)
            old = False

if new is True and old is True:
    Color.green("Все поля совпали")

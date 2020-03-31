import pyperclip
import re
import colorama
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)
colorama.init()


# newInput = "" -----------------------------+++++++++++++++++
# while (newInput != "F" or newInput != "f" or newInput != "exit") and newInput.__len__() < 100:
#     newInput = input('Вставьте xml данные новой, или введите F для загрузки из файла ' + 'new.xml' + "\n")
#     if newInput == "F" or newInput == "f":
#         with open('new.xml', 'r', encoding='UTF8') as file:
#             new = file.read()
#             break
#     if newInput != "F" and newInput.__len__() > 100:
#         new = newInput
#         break
#     if newInput == 'exit':
#         break
#     else:
#         print(Fore.RED + '   Данные не соответсвуют')


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


print(Fore.LIGHTGREEN_EX + '+++ Лишние в новой +++')
for x in set(new_Stat).difference(old_Stat):
    print(Fore.LIGHTGREEN_EX + x)


print(Fore.LIGHTRED_EX  + '+++ Лишние в старой +++')
for z in set(old_Stat).difference(new_Stat):
    print(Fore.LIGHTRED_EX + z)


print(Fore.BLUE + '------------------------------------------')


print(Fore.LIGHTGREEN_EX + '### Повторы в новой ###')
new_double = []
for x in new_Stat:
    if new_Stat.count(x) > 1:
        new_double.append(x)
        new_double.sort()

for x in new_double:
    print(Fore.LIGHTGREEN_EX + x)


print(Fore.LIGHTRED_EX + '### Повторы в старой ###')
old_double = []
for z in old_Stat:
    if old_Stat.count(z) > 1:
        old_double.append(z)
        old_double.sort()

for z in old_double:
    print(Fore.LIGHTRED_EX + z)




import json
import pyperclip
import re


from Converter_JJ import Color
from Converter_JJ import Novgorod
from Converter_JJ import Nakhodka

with open('Zapros.json', encoding='UTF8') as f:
    jason_all = json.load(f)
jason = jason_all['Zapros']



# --- Field.xml - Открытие и выделение полей из файла -------------------
with open('Field.xml', 'r', encoding='UTF8') as file:
    field = file.read()

scanField = r'field name=".+?"'
temp = re.findall(scanField, field)

resultField = []
for i in temp:
    resultField.append("{}".format(i[12:-1]))
# --- Field.xml - Обработка закончена -------------------


jasper = resultField

result = []

not_find = []

for z in jasper:

    app = False
    for x in jason:
        if x['caption'] == z:
            result.append(x)
            app = True
            break
    if not app:
        not_find.append("Не найдено ->  " + z)

field_ok = json.dumps(result, ensure_ascii=False, indent=4)



if len(not_find) > 0:
    Color.print_yellow('ПОЛЯ, НЕ НАЙДЕНЫЕ В ФАЙЛЕ "Zapros.json"')

    for i in not_find:
        Color.print_red(i)

if len(not_find) < 1:
    final_rezult = Nakhodka.zapros_past.replace('[$$]', field_ok)
    Color.print_w(final_rezult)
    pyperclip.copy(final_rezult)
    Color.print_green('Все поля найдены и скопированы в буфер обмена, добавлены условия.')


    # ColorModule.print_w(field_ok)
    # pyperclip.copy(field_ok)
    # ColorModule.print_green('СКОПИРОВАНЫ ТОЛЬКО ПОЛЯ')




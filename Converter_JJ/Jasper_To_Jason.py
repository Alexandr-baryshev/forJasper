import json
import pyperclip

from Converter_JJ import Regular
from Converter_JJ import ColorModule



with open('Zapros.json', encoding='UTF8') as f:
    jason_all = json.load(f)
jason = jason_all['Zapros']


with open('Zapros_past.json', encoding='UTF8') as ff:
    zapros_past = json.load(ff)
zapros = zapros_past['columns']


jasper = Regular.result

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

print("----------------------------------------------------------------------------")
ColorModule.print_w(json.dumps(result, ensure_ascii=False, indent=4))
pyperclip.copy(json.dumps(result, ensure_ascii=False, indent=4))
print("----------------------------------------------------------------------------")

if len(not_find) > 0:
    ColorModule.print_yellow('ПОЛЯ, НЕ НАЙДЕНЫЕ В ФАЙЛЕ "Zapros.json"')

    for i in not_find:
        ColorModule.print_red(i)

if len(not_find) < 1:
    ColorModule.print_green('ВСЕ ПОЛЯ НАЙДЕНЫ')


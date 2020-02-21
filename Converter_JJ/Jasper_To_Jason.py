import json
import pyperclip

from Converter_JJ import Regular
from Converter_JJ import ColorModule
from Converter_JJ import Zapros_Past

with open('Zapros.json', encoding='UTF8') as f:
    jason_all = json.load(f)
jason = jason_all['Zapros']

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

field_ok = json.dumps(result, ensure_ascii=False, indent=4)

if len(not_find) > 0:
    ColorModule.print_yellow('ПОЛЯ, НЕ НАЙДЕНЫЕ В ФАЙЛЕ "Zapros.json"')

    for i in not_find:
        ColorModule.print_red(i)

if len(not_find) < 1:
    final_rezult = Zapros_Past.zapros_past.replace('[$$]', field_ok)
    ColorModule.print_w(final_rezult)
    pyperclip.copy(final_rezult)
    ColorModule.print_green('Все поля найдены и скопированы в буфер обмена, добавлены условия.')

    # ColorModule.print_w(field_ok)
    # pyperclip.copy(field_ok)
    # ColorModule.print_green('СКОПИРОВАНЫ ТОЛЬКО ПОЛЯ')




import json
import pyperclip

from Converter_JJ import Field
from Converter_JJ import Color
from Converter_JJ import Novgorod

with open('Zapros.json', encoding='UTF8') as f:
    jason_all = json.load(f)
jason = jason_all['Zapros']

jasper = Field.result

def test_f(not_fin):
    if len(not_fin) > 0:
        Color.print_yellow('ПОЛЯ, НЕ НАЙДЕНЫЕ В ФАЙЛЕ "Zapros.json"')

        for i in not_fin:
            Color.print_red(i)


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

test_f(not_find)

if len(not_find) < 1:
    final_rezult = Novgorod.zapros_past.replace('[$$]', field_ok)
    Color.print_w(final_rezult)
    pyperclip.copy(final_rezult)
    Color.print_green('Все поля найдены и скопированы в буфер обмена, добавлены условия.')

    # ColorModule.print_w(field_ok)
    # pyperclip.copy(field_ok)
    # ColorModule.print_green('СКОПИРОВАНЫ ТОЛЬКО ПОЛЯ')




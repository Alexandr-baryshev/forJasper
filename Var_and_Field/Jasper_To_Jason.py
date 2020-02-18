import json
from Var_and_Field import regular

with open('Zapros.json', encoding='UTF8') as f:
    jason_all = json.load(f)
jason = jason_all['Zapros']

jasper = regular.result

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
print(json.dumps(result, ensure_ascii=False, indent=4))
print("----------------------------------------------------------------------------")


# ----Блок отвечающий за вывод цвета----
def out_red(text):
    print("\033[31m {}".format(text))


def out_yellow(text):
    print("\033[33m {}".format(text))

def out_green(text):
    print("\033[32m {}".format(text))


# ---------------------------------------
if len(not_find) > 0:
    out_yellow('')
    print('ПОЛЯ, НЕ НАЙДЕНЫЕ В ФАЙЛЕ "Zapros.json"')


    for i in not_find:
        out_red('')
        print(i)

if len(not_find) < 1:
    out_green('')
    print('ВСЕ ПОЛЯ НАЙДЕНЫ')

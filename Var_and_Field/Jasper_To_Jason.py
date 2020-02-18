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


# ---------------------------------------

out_yellow("")
print('ПОЛЯ НИЖЕ НЕ НАЙДЕНЫ В ФАЙЛЕ "Zapros.json"')

out_red("")

for i in not_find:
    print(i)

import json

with open('Zapros.json', encoding='UTF8') as f:
    jason_all = json.load(f)
jason = jason_all['Zapros']

jasper = [
    "Причина НС",
    "Дата рождения",
    "Основной диагноз по карте",
    "Номер полиса",
    "Серия полиса",
    "ФИО пациента",
    "Код (ОД)",
    "СМО код",
    "СМО ОКАТО",
    "Принято к оплате",
    "Номер вызова",
    "Идентификатор происшествия"
]

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
        not_find.append(z + "  <- Не найдено")


print("----------------------")
print(json.dumps(result, ensure_ascii=False, indent=4))
print("----------------------")

print("???????????????????????")
for i in not_find:
    print(i)

import json

with open('Zapros.json', encoding='UTF8') as f:
    jason_all = json.load(f)
jason = jason_all['Zapros']

jasper = [
    "Номер вызова",
    "Идентификатор происшествия",
    "Техника Позывной",
    "ФИО пациента",
    "ЛПУ",
    "Расшифровка (ОД)",
    "Код (ОД)",
    "Результат вызова",
    "ХУЙ знает что за поле",
    "Характер вызова по результату",
    "Возраст",
    "Адрес",
    "Заявитель",
    "Время регистрации",
    "Бригада Позывной"
]

result = []
not_find = []

b = -1


for z in jasper:
    b = b + 1
    a = -1
    for x in jason:
        a = a + 1
        if jason[a]['caption'] == jasper[b]:
            result.append(jason[a])
            break

        if jason[a]['caption'] != jasper[b] and len(jason) - 1 == a:
            not_find.append(jasper[b] + "  <- Не найдено")




print("----------------------")
print(json.dumps(result, ensure_ascii=False, indent=4))
print("----------------------")

print("???????????????????????")
for i in not_find:
    print(i)

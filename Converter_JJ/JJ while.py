import json

with open('Zapros.json', encoding='UTF8') as f:
    jason_all = json.load(f)
jason = jason_all['Zapros']

jasper = [
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
    "Номер вызова",
    "Идентификатор происшествия",
    "Заявитель",
    "Время регистрации",
    "Бригада Позывной"
]
result = []
not_find = []

b = -1

while len(jasper) - 1 > b:  # ЦИКЛ СМЕНЫ b
    b = b + 1
    a = -1
    while len(jason) - 1 > a:
        a = a + 1
        if jason[a]['caption'] == jasper[b]:
            result.append(jason[a])
            break

        if len(jason) - 1 == a and jason[a]['caption'] != jasper[b]:
            not_find.append(jasper[b] + " < Не найдено")



print("----------------------")
print(json.dumps(result, ensure_ascii=False, indent=4))
print("----------------------")

# ff = 0
# while len(not_find) > ff:
#     i = not_find[ff]
#     print(i)
#     ff = ff + 1


print("???????????????????????")
for i in not_find:
    print(i)


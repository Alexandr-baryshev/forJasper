import json

with open('Zapros.json', encoding='UTF8') as f:
    jason_all = json.load(f)
jason = jason_all['Zapros']

with open('regular.py', encoding='UTF8') as ff:
    jasper_all = ff
jasper = jasper_all['regular']

# jasper = [
#     "Регистрационный номер",
#     "Время регистрации",
#     "Расшифровка (ОД)",
#     "Наименование"
# ]

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

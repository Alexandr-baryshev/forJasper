jason = [
    '''
джейсон один
'''
    ,
    '''
джейсон два
 '''
    ,
    '''
джейсон три
 '''
    ,
    '''
джейсон четыре
 '''
    ,
    '''
джейсон шесть
 '''
]

jasper = ["один", "три", "два", "три"]

result = []

a = -1
b = 0
# print("a: {} b: {}".format(a, b))
while len(jasper) > len(result):
    # print("Цикл 1 - a: {} b: {}".format(a, b))
    a = a + 1
    if jason[a].__contains__(jasper[b]):
        result.append(jason[a])
        b = b + 1
        # print("Нашли в {} фразу".format(jason[a]))
    else:
        result.append(jasper[b] + " - Поле не найдено")
        # print("не нащли фразу {}".format(jasper[b]))
        b = b + 1
        a = 0

print(result)

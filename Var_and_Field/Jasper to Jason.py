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
    ,
    '''
джейсон семь
 '''
]

jasper = ["один", "три", "два", "шес", "вапкыв"]
find_ok = set()
result = []

b = -1
while len(jasper) - 1 > b:  # ЦИКЛ СМЕНЫ b
    b = b + 1
    a = -1
    res = False
    while len(jason) - 1 > a:
        a = a + 1
        if jason[a].__contains__(jasper[b]):
            result.append(jason[a])
            res = True
            find_ok.add(jasper[b])
            print("Поле совпало, b+1")

        if len(jason) - 1 == a and not res:
            result.append("не совпало {}".format(jasper[b]))
            print("Поле не совпало, a+1")


print(result)

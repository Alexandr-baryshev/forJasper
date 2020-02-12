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

result = []

b = -1

while len(jasper) >= len(result):  # ЦИКЛ СМЕНЫ b
    a = 0
    b = b + 1
    if len(jason) > a and len(jasper) > b and jason[a].__contains__(jasper[b]):
        result.append(jason[a])
        print("Поле совпало, b+1")

    else:
        while len(jason) > a and len(jasper) > b:  # ЦИКЛ СМЕНЫ a

            if not jason[a].__contains__(jasper[b]):
                a = a + 1
                print("Поле не совпало, a+1")

            else:
                result.append(jason[a])
                print("Поле совпало, возврат")
                break

print(result)

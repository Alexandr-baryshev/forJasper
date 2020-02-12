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

a = 0
b = 0

for jasper[b] in jason[a]:
    if jason[a].__contains__(jasper[b]):
        result.append(jason[a])
        b = b + 1
    else:
        a = a + 1


print(result)
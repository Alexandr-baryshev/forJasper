jason = [
    '''
{
джейсон один
},
'''
    ,
    '''
{
джейсон два
}
 '''
    ,
    '''
{
джейсон три
}
 '''
    ,
    '''
{
джейсон четыре
}
 '''
    ,
    '''
{
джейсон шесть
}
 '''
]

jasper = ["один", "три", "два"]

result = []

a = -1
b = 0

i = 0


while len(jasper) > len(result):
    a = a + 1
    if jason[a].__contains__(jasper[b]):
        result.append(jason[a])
        b = b + 1
    else:
        result.append(jasper[b] + " - Поле не найдено")
        b = b + 1
        a = 0


print(result)


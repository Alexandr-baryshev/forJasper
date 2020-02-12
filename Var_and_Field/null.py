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

jasper = ["один", "три", "два", "шесть"]

result = []

# a = -1
# b = 0

# while len(jasper) > len(result):
#     a = a + 1
#
#     while len(jasper) > len(result):
#
#         if jason[a].__contains__(jasper[b]):
#             result.append(jason[a])
#             break
#
#         elif len(jasper) > len(result):
#             b = b + 1
#
#         else:
#             result.append(jasper[b] + " - Поле не найдено")
#
# print(result)

a = 0
b = -1

while len(jasper) > len(result):  # ЦИКЛ СМЕНЫ b
    b = b + 1
    if jason[a].__contains__(jasper[b]):
        result.append(jason[a])
        print("Поле совпало, b+1")

    else:
        while len(jason) > a:    # ЦИКЛ СМЕНЫ a

            if not jason[a].__contains__(jasper[b]):
                a = a + 1

            else:
                result.append(jason[a])
                a = 0
                print("Поле совпало, возврат")
                break

print(result)

import builtins
import re
import sys

a = 100

# ВСЕ АНАЛОГИЧНО

a.__add__(5)
builtins.int.__add__(100, 5)

x = builtins.int.__add__
x(100, 5)

y = builtins.int
y.__add__(100, 5)

tt = 0
ww = 0


class Huita:

    def my_fun1(self):
        if self > 5:
            print('U больше 5')
        if self < 5 and self != 0:
            print(self)
        if self == 0:
            return 55555


def my_sum(aa, bb):
    if aa > bb:
        c = aa - bb
        return c
    if aa < bb:
        c = bb - aa
        return c
    if aa == bb:
        c = aa * bb
        return c




yy = my_sum(5, 5)

print()

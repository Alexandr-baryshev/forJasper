import builtins
import re
import sys


# a = 100

# --- Встроеные классы и фунции -----------------------

# a.__add__(5)
# builtins.int.__add__(100, 5)
#
# x = builtins.int.__add__
# x(100, 5)
#
# y = builtins.int
# y.__add__(100, 5)


# --- ТЕСТЫ своих классов и функций -------------------

class my_class(builtins.int):

    def my_fun(self: int):
        if self > 5:
            print('больше 5')
        if self < 5 and self != 0:
            print(str(self) + " - меньше 5")
        if self == 0:
            return 55555

    def my_sum(self, x):
        if self > x:
            return self - x
        if self < x:
            return x - self
        if self == x:
            return self * x


h = my_class

s = h.my_fun(h.my_sum(0, 0))



print(s)



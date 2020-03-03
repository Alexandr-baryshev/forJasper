import builtins
import re


a = 100

# ВСЕ АНАЛОГИЧНО

a.__add__(5)
builtins.int.__add__(100, 5)

x = builtins.int.__add__
x(100, 5)

y = builtins.int
y.__add__(100, 5)


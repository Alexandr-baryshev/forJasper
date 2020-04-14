import pyperclip
from colorama import Fore

# ФОРМИРОВАНИ ПО ПРИНЦИПУ - C1 R1,  C1 R2,  C1 R3, и тд. * простое выделение столбцов в редакторе

# Образец переменной
'''
	<variable name="R1 C1" class="java.lang.Integer" calculation="DistinctCount">
		<variableExpression><![CDATA[$V{R1} && $V{C1} ? $F{Идентификатор происшествия} : null]]></variableExpression>
	</variable>
'''

print("-------------- Содержимое буфера ---------------------------------------------------------")

# Цикл проверки содержимого буфера обмена
q = ""
while q != "y":
    variable = pyperclip.paste()
    print(Fore.LIGHTGREEN_EX + variable)
    q = input(Fore.RESET + "-------------- Продолжить? -------------- " + Fore.RED + "Y / N -> ").casefold()
    if q == "n":
        exit()

# --- C СТОЛБЕЦ замена X раз ----------------------->

p1 = int(input("Старт строки от - "))
p2 = int(input("Размер строки - "))
p3 = int(input("Старт колонки от - "))
p4 = int(input("Размер клонки - "))


# Приоритет колонки
def Cx_Rx(R_Start=p1, R_Size=p2, C_Start=p3, C_Size=p4):
    allResult = ""
    row = variable.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}")
    c = C_Start
    while c <= C_Size:
        rowResult = row.format(c)

        # --- R СТРОКА замена X раз ->
        column = rowResult.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}")
        r = R_Start
        while r <= R_Size:
            columnResult = column.format(r)
            allResult = allResult + columnResult + "\r\n"
            # print(columnResult)
            r = r + 1
        # --- СТОЛБЕЦ конец - ///

        c = c + 1
    pyperclip.copy(allResult)
    return allResult


# Приоритет строки
def Rx_Cx(R_Start=p1, R_Size=p2, C_Start=p3, C_Size=p4):
    allResult = ""
    row = variable.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}")
    r = R_Start
    while r <= R_Size:
        rowResult = row.format(r)

        # --- R СТРОКА замена X раз ->
        column = rowResult.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}")
        c = C_Start
        while c <= C_Size:
            columnResult = column.format(c)
            allResult = allResult + columnResult + "\r\n"
            c = c + 1
        # --- СТОЛБЕЦ конец - ///

        r = r + 1
    pyperclip.copy(allResult)
    return allResult


prioritet = ""

while prioritet != "c" or prioritet != "r":
    prioritet = input(Fore.BLUE + "Приоритет строки - R / Приоритет колонки - С / Выход - E -> ").casefold()
    if prioritet == "c":
        Cx_Rx()
        print(Fore.LIGHTGREEN_EX + Cx_Rx())
    if prioritet == "r":
        Rx_Cx()
        print(Fore.LIGHTGREEN_EX + Rx_Cx())
    if prioritet == "e":
        exit()


# --- СТРОКА конец ------------------------------ ///

import pyperclip

# ФОРМИРОВАНИ ПО ПРИНЦИПУ - C1 R1,  C1 R2,  C1 R3, и тд. * простое выделение столбцов в редакторе
# --- ПЕРЕМЕННАЯ ----------------------------------------------------------------------

q = input("Встаить содержимое из буфера?  \n  Y / N  \n")


if q == "Y" or q == "y":
    variable = pyperclip.paste()
else:
    exit()

'''
	<variable name="R1 C1" class="java.lang.Integer" calculation="Sum">
		<variableExpression><![CDATA[$V{R1} ? $V{C1} : null]]></variableExpression>
	</variable>
'''


# --- C СТОЛБЕЦ замена X раз ----------------------->


def Cx_Rx(C_Start=int(input("Старт колонки от - ")), C_Size=int(input("Размер клонки - ")),
          R_Start=int(input("Старт строки от - ")), R_Size=int(input("Размер строки - "))):
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


# --- СТРОКА конец ------------------------------ ///

Cx_Rx()

print(Cx_Rx())

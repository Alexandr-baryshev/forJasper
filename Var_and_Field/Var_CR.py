import pyperclip

# ФОРМИРОВАНИ ПО ПРИНЦИПУ - C1 R1,  C1 R2,  C1 R3, и тд. * простое выделение столбцов в редакторе
# --- ПЕРЕМЕННАЯ ----------------------------------------------------------------------

variable = '''
	<variable name="R1 C1" class="java.lang.Integer" calculation="Sum">
		<variableExpression><![CDATA[$V{R1} ? $V{C1} : null]]></variableExpression>
	</variable>
 '''


# --- C СТОЛБЕЦ замена X раз ----------------------->


def Cx_Rx(C_Start, C_Max, R_Start, R_Max):
    allResult = ""
    row = variable.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}")
    c = C_Start
    while c <= C_Max:
        rowResult = row.format(c)

        # --- R СТРОКА замена X раз ->
        column = rowResult.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}")
        r = R_Start
        while r <= R_Max:
            columnResult = column.format(r)
            allResult = allResult + columnResult + "\r\n"
            # print(columnResult)
            r = r + 1
        # --- СТОЛБЕЦ конец - ///

        c = c + 1
    pyperclip.copy(allResult)
    return allResult


# --- СТРОКА конец ------------------------------ ///

print(Cx_Rx(1, 3, 1, 3))


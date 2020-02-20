import pyperclip
# ФОРМИРОВАНИ ПО ПРИНЦИПУ - C1 R1,  C1 R2,  C1 R3, и тд. * простое выделение столбцов в редакторе
# --- ПЕРЕМЕННАЯ ----------------------------------------------------------------------

variable = '''
	<variable name="R1 C1" class="java.lang.Integer" calculation="Sum">
		<variableExpression><![CDATA[$V{R1} ? $V{C1} : null]]></variableExpression>
	</variable>
 '''
# -------------------------------------------------------------------

allResult = ""

# --- C СТОЛБЕЦ замена X раз ----------------------->
row = variable.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}")
c = 1
while c <= 1:
    rowResult = row.format(c)

    # --- R СТРОКА замена X раз ->
    column = rowResult.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}")
    r = 1
    while r <= 10:
        columnResult = column.format(r)
        allResult = allResult + columnResult + "\r\n"
        print(columnResult)
        r = r + 1
    # --- СТОЛБЕЦ конец - ///

    c = c + 1
# --- СТРОКА конец ------------------------------ ///




# --- КОПИЯ ВСЕГО
pyperclip.copy(allResult)

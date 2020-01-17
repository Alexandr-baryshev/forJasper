import clipboard
# ФОРМИРОВАНИ ПО ПРИНЦИПУ - R1 C1,  R1 C2,  R1 C3, и тд. * простое выделение строк в редакторе
# --- ПЕРЕМЕННАЯ ----------------------------------------------------------------------

variable = '''
	<variable name="R1 C7" class="java.lang.Integer" calculation="Sum">
		<variableExpression><![CDATA[$V{R1} ? $V{C7} : null]]></variableExpression>
	</variable>
 '''
# -------------------------------------------------------------------

allResult = ""

# --- R СТРОКА замена X раз ----------------------->
row = variable.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}")
r = 1
while r <= 20:
    rowResult = row.format(r)

    # --- C СТОЛБЕЦ замена X раз ->
    column = rowResult.replace("{", "{{").replace("}", "}}").replace("C7", "C{0}")
    c = 7
    while c <= 8:
        columnResult = column.format(c)
        allResult = allResult + columnResult + "\r\n"
        print(columnResult)
        c = c + 1
    # --- СТОЛБЕЦ конец - ///

    r = r + 1
# --- СТРОКА конец ------------------------------ ///




# --- КОПИЯ ВСЕГО
clipboard.copy(allResult)

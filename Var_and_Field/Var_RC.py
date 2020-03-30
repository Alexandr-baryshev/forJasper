import pyperclip
# ФОРМИРОВАНИ ПО ПРИНЦИПУ - R1 C1,  R1 C2,  R1 C3, и тд. * простое выделение строк в редакторе
# --- ПЕРЕМЕННАЯ ----------------------------------------------------------------------

variable = '''
	<variable name="R1 C1" class="java.lang.Integer" calculation="DistinctCount">
		<variableExpression><![CDATA[$V{R1} && $V{C1} ? $F{Идентификатор происшествия} : null]]></variableExpression>
	</variable>
 '''
# -------------------------------------------------------------------

allResult = ""

# --- R СТРОКА замена X раз ----------------------->
row = variable.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}")
r = 1
while r <= 8:
    rowResult = row.format(r)

    # --- C СТОЛБЕЦ замена X раз ->
    column = rowResult.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}")
    c = 1
    while c <= 6:
        columnResult = column.format(c)
        allResult = allResult + columnResult + "\r\n"
        print(columnResult)
        c = c + 1
    # --- СТОЛБЕЦ конец - ///

    r = r + 1
# --- СТРОКА конец ------------------------------ ///




# --- КОПИЯ ВСЕГО
pyperclip.copy(allResult)

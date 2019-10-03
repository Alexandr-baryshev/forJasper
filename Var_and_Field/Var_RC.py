import clipboard

# --- ПЕРЕМЕННАЯ ----------------------------------------------------------------------

variable = '''
	<variable name="R1 &amp; C1" class="java.lang.Integer" calculation="DistinctCount">
		<variableExpression><![CDATA[$V{R1} && $V{C1} ? $F{Идентификатор происшествия} : null]]></variableExpression>
	</variable>
 '''
# -----------------

allResult = ""


# --- R СТРОКА замена 11 раз ----------------------->
row = variable.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}")
r = 1
while r <= 11:
    rowResult = row.format(r)

    # --- C СТОЛБЕЦ замена 31 раз ->
    column = rowResult.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}")
    c = 1
    while c <= 31:
        columnResult = column.format(c)
        allResult = allResult + columnResult + "\r\n"
        print(columnResult)
        c = c + 1
    # --- СТОЛБЕЦ конец - ///

    r = r + 1
# --- СТРОКА конец ------------------------------ ///




# --- КОПИЯ ВСЕГО
clipboard.copy(allResult)

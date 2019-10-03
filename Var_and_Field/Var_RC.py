import clipboard

# ---Замена R ----------------------------------------------------------------------------------------

variable = '''
	<variable name="R1 &amp; C1" class="java.lang.Integer" calculation="DistinctCount">
		<variableExpression><![CDATA[$V{R1} && $V{C1} ? $F{Идентификатор происшествия} : null]]></variableExpression>
	</variable>
 '''

row = variable.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}").replace("R1", "R{0}")
rowALL = ""



# ---подцикл / НАЧАЛО -- Замена C при постоянной R ------------------------------------------------------------------
i = 1
while i <= 31:
    rowResult = row.format(i)
    rowALL = rowALL + rowResult + "\r\n"
    print(rowResult)
    i = i + 1
# ---подцикл / КОНЕЦ -- Замена C при постоянной R ------------------------------------------------------------------


# --- КОПИЯ ВСЕГО
clipboard.copy(rowALL)

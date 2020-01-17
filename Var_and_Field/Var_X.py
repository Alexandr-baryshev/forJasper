import clipboard

# --- ПЕРЕМЕННАЯ ----------------------------------------------------------------------

variable = '''
	<variable name="R1 C10" class="java.lang.Long" calculation="Sum">
		<variableExpression><![CDATA[$V{R1} ?  ($V{R1 C9} / 60) * $V{C10} : null]]></variableExpression>
	</variable>
 '''
# -------------------------------------------------------------------

result = ""

cell = variable.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}")

i = 1
while i <= 20:
    cellResult = cell.format(i)
    result = result + cellResult + "\r\n"
    print(cellResult)
    i = i + 1

clipboard.copy(result)
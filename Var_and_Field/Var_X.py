import clipboard

# --- ПЕРЕМЕННАЯ ----------------------------------------------------------------------

variable = '''
	<variable name="R11 &amp; C1" class="java.lang.Integer" calculation="DistinctCount">
		<variableExpression><![CDATA[$V{R11} && $V{C1} ? $F{Идентификатор происшествия} : null]]></variableExpression>
	</variable>
 '''
# -------------------------------------------------------------------

result = ""

cell = variable.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}").replace("01", "{00}")

i = 1
while i <= 31:
    cellResult = cell.format(i)
    result = result + cellResult + "\r\n"
    print(cellResult)
    i = i + 1

clipboard.copy(result)
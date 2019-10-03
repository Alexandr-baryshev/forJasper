import clipboard

# --- ПЕРЕМЕННАЯ ----------------------------------------------------------------------

variable = '''
	<variable name="C1_sum" class="java.lang.Integer">
		<variableExpression><![CDATA[$V{R1 & C1} + $V{R2 & C1} + $V{R3 & C1} + $V{R4 & C1} + $V{R5 & C1} + $V{R6 & C1} + $V{R7 & C1} + $V{R8 & C1} + $V{R9 & C1} + $V{R10 & C1} + $V{R11 & C1}]]></variableExpression>
	</variable>
 '''
# -------------------------------------------------------------------

result = ""

cell = variable.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}")

i = 1
while i <= 31:
    cellResult = cell.format(i)
    result = result + cellResult + "\r\n"
    print(cellResult)
    i = i + 1

clipboard.copy(result)
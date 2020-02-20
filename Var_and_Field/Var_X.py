import pyperclip

# --- ПЕРЕМЕННАЯ ----------------------------------------------------------------------

variable = '''
	<variable name="C3" class="java.lang.Boolean">
		<variableExpression><![CDATA[true]]></variableExpression>
	</variable>
 '''
# -------------------------------------------------------------------

result = ""

cell = variable.replace("{", "{{").replace("}", "}}").replace("C3", "C{0}")

i = 3
while i <= 19:
    cellResult = cell.format(i)
    result = result + cellResult + "\r\n"
    print(cellResult)
    i = i + 1

pyperclip.copy(result)
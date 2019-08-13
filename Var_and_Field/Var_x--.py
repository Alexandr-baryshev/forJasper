import clipboard


bas_template = '''
	<variable name="R_1 &amp; C_4" class="java.lang.Integer" calculation="DistinctCount">
		<variableExpression><![CDATA[$V{R_1} && $V{C_4} ?  $F{Идентификатор происшествия} : null]]></variableExpression>
	</variable>
 '''

template = bas_template.replace("{", "{{").replace("}", "}}").replace("R_1", "R_{0}")

all_gotovo = ""
i = 1
while i < 7:
    gotovo = template.format(i)
    all_gotovo = all_gotovo + gotovo + "\r\n"
    print(gotovo)
    i = i + 1

clipboard.copy(all_gotovo)
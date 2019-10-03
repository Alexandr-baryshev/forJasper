import clipboard


bas_template = '''
	<variable name="R11 &amp; C1" class="java.lang.Integer" calculation="DistinctCount">
		<variableExpression><![CDATA[$V{R11} && $V{C1} ? $F{Идентификатор происшествия} : null]]></variableExpression>
	</variable>
 '''

template = bas_template.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}").replace("01", "{00}")

all_gotovo = ""
i = 1
while i <= 31:
    gotovo = template.format(i)
    all_gotovo = all_gotovo + gotovo + "\r\n"
    print(gotovo)
    i = i + 1

clipboard.copy(all_gotovo)
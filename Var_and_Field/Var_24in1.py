import pyperclip
import re


bas_template = '''
	<variable name="R1_sum" class="java.lang.Integer">
		<variableExpression><![CDATA[$V{R1 & C1} + $V{R1 & C2} + $V{R1 & C3} +
$V{R1 & C4} + $V{R1 & C5} + $V{R1 & C6} +
$V{R1 & C7} + $V{R1 & C8} + $V{R1 & C9} +
$V{R1 & C10} + $V{R1 & C11} + $V{R1 & C12} + $V{R1 & C13} +
$V{R1 & C14} + $V{R1 & C15} + $V{R1 & C16} +$V{R1 & C17}]]></variableExpression>
	</variable>
 '''

template = bas_template.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}_")


gotovo = template.format("тест")

print(gotovo)


pyperclip.copy(gotovo)
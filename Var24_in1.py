import clipboard
import re


bas_template = '''
	<variable name="СкораяАбс_Сумма" class="java.lang.Integer">
		<variableExpression><![CDATA[SUM($V{СкораяАбс_0},$V{СкораяАбс_1},$V{СкораяАбс_2},$V{СкораяАбс_3},
		$V{СкораяАбс_4},$V{СкораяАбс_5},$V{СкораяАбс_6},$V{СкораяАбс_7},$V{СкораяАбс_8},$V{СкораяАбс_9},
		$V{СкораяАбс_10},$V{СкораяАбс_11},$V{СкораяАбс_12},$V{СкораяАбс_13},$V{СкораяАбс_14},$V{СкораяАбс_15},
		$V{СкораяАбс_16},$V{СкораяАбс_17},$V{СкораяАбс_18},$V{СкораяАбс_19}, $V{СкораяАбс_20},$V{СкораяАбс_21},
		$V{СкораяАбс_22},$V{СкораяАбс_23} )]]></variableExpression>
	</variable>
 '''

template = bas_template.replace("{", "{{").replace("}", "}}").replace("СкораяАбс_", "{0}_")


gotovo = template.format("тест")
print(gotovo)


clipboard.copy(gotovo)
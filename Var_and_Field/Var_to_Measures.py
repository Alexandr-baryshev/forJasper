import pyperclip
import re


bas_template = '''
	<variable name="ПередачВызСумВрем" class="java.lang.Long" resetType="Group" resetGroup="по Позывной" calculation="Sum">
		<variableExpression><![CDATA[$F{Время регистрации} != null && $F{Время получения команды на выезд}  != null ?
( $F{Время получения команды на выезд}.getTime() - $F{Время регистрации}.getTime() ) / 1000 : null]]></variableExpression>
	</variable>
	<variable name="ПередачВызКол-во" class="java.lang.Integer" resetType="Group" resetGroup="по Позывной" calculation="DistinctCount">
		<variableExpression><![CDATA[$F{Время регистрации} != null && $F{Время получения команды на выезд}  != null ?
$F{Идентификатор происшествия} : null]]></variableExpression>
	</variable>
	<variable name="ПередачВыз" class="java.lang.Long" resetType="Group" resetGroup="по Позывной">
		<variableExpression><![CDATA[$V{ПередачВызСумВрем} / $V{ПередачВызКол-во}]]></variableExpression>
	</variable>
 '''

template = bas_template.replace("{", "{{").replace("}", "}}").replace("variable", "{0}")

template = re.sub(r'class=".+?"', 'class="{1}"', template)

template = re.sub(r'resetType=".+?"', '', template)
template = re.sub(r'resetGroup=".+?"', '', template)

gotovo = template.format("measure", "java.lang.Object")

print(gotovo)

pyperclip.copy(gotovo)



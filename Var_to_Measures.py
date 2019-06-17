import clipboard
import re


bas_template = '''
	<variable name="ВыездаСумВрем" class="java.lang.Long" resetType="Group" resetGroup="по Позывной" calculation="Sum">
		<variableExpression><![CDATA[$F{Время выезда} != null && $F{Время получения команды на выезд}  != null ?
( $F{Время выезда}.getTime() - $F{Время получения команды на выезд}.getTime() ) / 1000 : null]]></variableExpression>
	</variable>
	<variable name="ВыездаКол-во" class="java.lang.Integer" resetType="Group" resetGroup="по Позывной" calculation="DistinctCount">
		<variableExpression><![CDATA[$F{Время выезда} != null && $F{Время получения команды на выезд}  != null ?
$F{Идентификатор происшествия} : null]]></variableExpression>
	</variable>
	<variable name="Выезда" class="java.lang.Long" resetType="Group" resetGroup="по Позывной">
		<variableExpression><![CDATA[$V{ВыездаСумВрем} / $V{ВыездаКол-во}]]></variableExpression>
	</variable>
 '''

template = bas_template.replace("{", "{{").replace("}", "}}").replace("variable", "{0}")

template = re.sub(r'class=".+?"', 'class="{1}"', template)

template = re.sub(r'resetType=".+?"', '', template)
template = re.sub(r'resetGroup=".+?"', '', template)

gotovo = template.format("measure", "java.lang.Long")

print(gotovo)

clipboard.copy(gotovo)



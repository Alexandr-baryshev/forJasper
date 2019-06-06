import clipboard
import uuid
import re

all_gotovo = ""

#Первая серия переменных +

bas_template = '''
	<variable name="БригадаСумВремя(sec)_0" class="java.lang.Long" calculation="Sum">
		<variableExpression><![CDATA[$V{Бригада_BooL} && $V{BooL_0}  ?
( $F{Время возврата на базу}.getTime() - $F{Время выезда}.getTime() ) / 1000 : null]]></variableExpression>
	</variable>
 '''

template = bas_template.replace("{", "{{").replace("}", "}}").replace("_0", "_{0}")

i = 0

while i < 24:
    gotovo = template.format(i)
    all_gotovo = all_gotovo + gotovo + "\r\n"
    print(gotovo)
    i = i + 1

#Вторая серия переменных

bas_template = '''
	<variable name="БригадаКол-во_0" class="java.lang.Integer" calculation="Count">
		<variableExpression><![CDATA[$V{BooL_0} && $V{Бригада_BooL} ? 1 : null]]></variableExpression>
	</variable>
 '''

template = bas_template.replace("{", "{{").replace("}", "}}").replace("_0", "_{0}")

i = 0

while i < 24:
    gotovo = template.format(i)
    all_gotovo = all_gotovo + gotovo + "\r\n"
    print(gotovo)
    i = i + 1

#Третяя серия переменных

bas_template = '''
	<variable name="Бригада_0" class="java.lang.Long">
		<variableExpression><![CDATA[$V{БригадаСумВремя(sec)_0}/$V{БригадаКол-во_0}]]></variableExpression>
	</variable>
 '''

template = bas_template.replace("{", "{{").replace("}", "}}").replace("_0", "_{0}")

i = 0

while i < 24:
    gotovo = template.format(i)
    all_gotovo = all_gotovo + gotovo + "\r\n"
    print(gotovo)
    i = i + 1

#Копирование всех серий в буфер

clipboard.copy(all_gotovo)
import clipboard
import uuid
import re

all_gotovo = ""

#Первая серия переменных +

bas_template = '''
	<variable name="ГоспитСумВремя(sec)_0" class="java.lang.Long" calculation="Sum">
		<variableExpression><![CDATA[$V{Госпит_BooL} && $V{BooL_0}  ?
( $F{Время окончания транспортировки}.getTime() - $F{Время убытия с места происшествия}.getTime() ) / 1000 : null]]></variableExpression>
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
	<variable name="ГоспитКол-во_0" class="java.lang.Integer" calculation="Count">
		<variableExpression><![CDATA[$V{BooL_0} && $V{Госпит_BooL} ? 1 : null]]></variableExpression>
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
	<variable name="Госпит_0" class="java.lang.Long">
		<variableExpression><![CDATA[$V{ГоспитСумВремя(sec)_0}/$V{ГоспитКол-во_0}]]></variableExpression>
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
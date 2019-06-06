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

#Генерация полей

bas_template = '''
			<textField isBlankWhenNull="true">
				<reportElement style="ДанныеПОДСтолбцов3" x="605" y="0" width="40" height="15" uuid="401df5b6-f838-4a3a-9c53-48f940f5d3b0"/>
				<textFieldExpression><![CDATA[((long)($V{Бригада_0} / 3600)) + ":" + ((long)(($V{Бригада_0} % 3600)/60)) + ":" +((long)($V{Бригада_0} % 3600)%60 )]]></textFieldExpression>
			</textField>
 '''


template = bas_template.replace("{", "{{").replace("}", "}}").replace("_0", "_{0}").replace('y="0"', 'y="{1}"')

template = re.sub(r'uuid=".+?"', 'uuid="{2}"', template)

i = 0
while i < 24:
    y = 15 * i
    gotovo = template.format(i, y, str(uuid.uuid4()),)
    all_gotovo = all_gotovo + gotovo + "\r\n"
    print(gotovo)
    i = i + 1

#Копирование всех серий в буфер

clipboard.copy(all_gotovo)
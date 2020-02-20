import re

xml_string = '''
	<field name="Дней" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Месяцев" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Место регистрации" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Характер вызова по результату" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Пол пациента код" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Лет" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Идентификатор происшествия" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
'''

scanText = r'name=".+?"'
temp = re.findall(scanText, xml_string)
result = []


for i in temp:
    result.append("{}".format(i[6:-1]))


# print(result)

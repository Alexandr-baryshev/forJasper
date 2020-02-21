import re

xml_string = '''
	<field name="ЛПУ" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Код (ОД)" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Код (ПО)" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Номер вызова" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Время регистрации" class="java.util.Date">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Причины отказа в госпитализации" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Блок (ОД)" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Блок (ПО)" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Старший бригады" class="java.lang.String"/>
	<field name="Идентификатор происшествия" class="java.lang.Integer">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
'''

scanText = r'name=".+?"'
temp = re.findall(scanText, xml_string)
result = []


for i in temp:
    result.append("{}".format(i[6:-1]))


# print(result)

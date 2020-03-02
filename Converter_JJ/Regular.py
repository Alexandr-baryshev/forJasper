import re

xml_string = '''
	<field name="Идентификатор происшествия" class="java.lang.Integer">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Время регистрации" class="java.util.Date">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Причина НС" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Амбулаторно" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Признак безрезультатного вызова" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Причина завершения происшествия (результат)" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Характер вызова по результату" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Характер по результату Транспортировка" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Признак роды или патологии беременности по результату" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Признак несчастного случая по результату" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Признак внезапного заболевания по результату" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Характер вызова" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Характер вазова Транспортировка" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Признак роды или патологии беременности характер вызова" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Признак несчастного случая характер вызова" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Признак внезапного заболевания характер вызова" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="СЛР смерть наступила" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Лет" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Месяцев" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Дней" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Наименование типа сил и средств" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="ЛПУ" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Место регистрации" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Время возврата на базу" class="java.util.Date">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Время прибытия на место происшествия" class="java.util.Date">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Время получения команды на выезд" class="java.util.Date">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Время убытия с места происшествия" class="java.util.Date">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Время выезда" class="java.util.Date">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
'''

scanText = r'name=".+?"'
temp = re.findall(scanText, xml_string)
result = []

for i in temp:
    result.append("{}".format(i[6:-1]))

for i in temp:
    print(i)

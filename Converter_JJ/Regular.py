import re

xml_string = '''
	<field name="Наименование типа сил и средств" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Время прибытия на место происшествия" class="java.util.Date">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Время убытия с места происшествия" class="java.util.Date">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Время выезда" class="java.util.Date">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="СЛР вид остановки сердца" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="СЛР смерть наступила" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="СЛР результат" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Проведена СЛР" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="ФИО пациента" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="ЛПУ" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Расшифровка (ОД)" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Пол" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Возраст" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Состав бригады" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Старший врач подстанции" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Адрес" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Номер вызова" class="java.lang.Number">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Время регистрации" class="java.util.Date">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Повод" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
	<field name="Описание повода" class="java.lang.String">
		<fieldDescription><![CDATA[]]></fieldDescription>
	</field>
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

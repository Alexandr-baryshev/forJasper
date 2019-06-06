import clipboard


bas_template = '''
	<variable name="Возврат_0" class="java.lang.Long">
		<variableExpression><![CDATA[$V{ВозвратСумВремя(sec)_0}/$V{ВозвратКол-во_0}]]></variableExpression>
	</variable>
 '''

template = bas_template.replace("{", "{{").replace("}", "}}").replace("_0", "_{0}")

all_gotovo = ""
i = 0
while i < 24:
    gotovo = template.format(i)
    all_gotovo = all_gotovo + gotovo + "\r\n"
    print(gotovo)
    i = i + 1

clipboard.copy(all_gotovo)
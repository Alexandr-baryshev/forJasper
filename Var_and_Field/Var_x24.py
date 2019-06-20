import clipboard


bas_template = '''
	<variable name="ГоспитСумВремя(sec)_0" class="java.lang.Long" calculation="Sum">
		<variableExpression><![CDATA[$V{Госпит_BooL} && $V{BooL_0}  ?
( $F{Время убытия с места происшествия}.getTime() - $F{Время окончания транспортировки}.getTime()  ) / 1000 : null]]></variableExpression>
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
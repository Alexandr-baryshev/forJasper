
bas_template = '''
<variable name="Передача_0" class="java.lang.Long" calculation="Sum">
<variableExpression><![CDATA[$V{BooL_0} ?  $V{ПЕРЕДАЧИ}/$V{Всего_0} : null]]></variableExpression>
</variable>
'''

template = bas_template.replace("{", "{{").replace("}", "}}").replace("_0", "_{0}")

i = 0
while i < 24:
    gotovo = template.format(i)
    print(gotovo)
    i = i + 1

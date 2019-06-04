
template = '''
<variable name="Передача_{0}" class="java.lang.Long" calculation="Sum">
<variableExpression><![CDATA[$V{{BooL_{0}}} ?  $V{{ПЕРЕДАЧИ}}/$V{{Всего_{0}}} : null]]></variableExpression>
</variable>
'''

i = 0
while i < 24:
    gotovo = template.format(i)
    print(gotovo)
    i = i + 1




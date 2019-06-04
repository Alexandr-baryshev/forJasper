import uuid

template = '''
<textField>
<reportElement style="ДанныеПОДСтолбцов" x="260" y="{0}" width="50" height="15" uuid="{1}">
<property name="com.jaspersoft.studio.unit.height" value="px"/>
</reportElement>
<textFieldExpression><![CDATA[$V{{Передача_{2}}}/60000  + ":" + $V{{Передача_{2}}}/60000%1000]]></textFieldExpression>

</textField>
'''

i = 0
while i < 24:
    y = 15 * i
    gotovo = template.format(y, str(uuid.uuid4()), i)
    print(gotovo)
    i = i + 1




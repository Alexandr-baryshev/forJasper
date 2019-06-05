import clipboard
import uuid
import re

bas_template = '''
			<textField>
				<reportElement style="ДанныеПОДСтолбцов" x="310" y="0" width="40" height="15" uuid="1124ed84-8d0f-47ec-a4a3-77899eb463c4">
					<property name="com.jaspersoft.studio.unit.height" value="px"/>
				</reportElement>
				<textFieldExpression><![CDATA[$V{Выезды_0}]]></textFieldExpression>
			</textField>
'''
template = bas_template.replace("{", "{{").replace("}", "}}").replace("_0", "_{0}").replace('y="0"', 'y="{1}"')

template = re.sub(r'uuid=".+?"', 'uuid="{2}"', template)

all_gotovo = ""
i = 0
while i < 24:
    y = 15 * i
    gotovo = template.format(i, y, str(uuid.uuid4()),)
    all_gotovo = all_gotovo + gotovo + "\r\n"
    print(gotovo)
    i = i + 1

clipboard.copy(all_gotovo)


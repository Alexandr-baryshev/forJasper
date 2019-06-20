import clipboard
import uuid
import re

bas_template = '''
		<textField isBlankWhenNull="true">
				<reportElement style="ДанныеПОДСтолбцов3" x="560" y="0" width="60" height="15" uuid="bd9aa1d1-870f-467e-a8ff-4094ae915475">
					<property name="com.jaspersoft.studio.unit.width" value="px"/>
				</reportElement>
				<textFieldExpression><![CDATA[((long)($V{Госпит_0} / 3600)) + ":" + ((long)(($V{Госпит_0} % 3600)/60)) + ":" +((long)($V{Госпит_0} % 3600)%60 )]]></textFieldExpression>
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


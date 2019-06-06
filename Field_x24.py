import clipboard
import uuid
import re

bas_template = '''
			<textField isBlankWhenNull="true">
				<reportElement style="ДанныеПОДСтолбцов3" x="550" y="0" width="55" height="15" uuid="a2680c9e-d00d-49cd-9458-a27949d8e024"/>
				<textFieldExpression><![CDATA[((long)($V{Возврат_0} / 3600)) + ":" + ((long)(($V{Возврат_0} % 3600)/60)) + ":" +((long)($V{Возврат_0} % 3600)%60 )]]></textFieldExpression>
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


import clipboard
import uuid
import re

bas_template = '''
			<textField isBlankWhenNull="true">
				<reportElement style="ДанныеПОДСтолбцов3" x="645" y="0" width="40" height="15" uuid="34258d57-bcc3-497a-be43-82709e777cd4"/>
				<textFieldExpression><![CDATA[((long)($V{Станция_0} / 3600)) + ":" + ((long)(($V{Станция_0} % 3600)/60)) + ":" +((long)($V{Станция_0} % 3600)%60 )]]></textFieldExpression>
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


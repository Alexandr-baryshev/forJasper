import clipboard
import uuid
import re

bas_template = '''
			<textField isStretchWithOverflow="true" isBlankWhenNull="true">
				<reportElement style="Ячейка" stretchType="RelativeToBandHeight" x="440" y="50" width="110" height="20" uuid="1815ec41-e6b4-47e0-85b0-13417c3a6f75"/>
				<textFieldExpression><![CDATA[$V{R_1 & C_4}]]></textFieldExpression>
			</textField>
 '''


template = bas_template.replace("{", "{{").replace("}", "}}").replace("R_1", "R_{0}").replace('y="50"', 'y="{1}"')

template = re.sub(r'uuid=".+?"', 'uuid="{2}"', template)

all_gotovo = ""
i = 1
while i < 7:
    y = 20 * i
    gotovo = template.format(i, y, str(uuid.uuid4()),)
    all_gotovo = all_gotovo + gotovo + "\r\n"
    print(gotovo)
    i = i + 1

clipboard.copy(all_gotovo)


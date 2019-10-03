import clipboard
import uuid
import re

bas_template = '''
			<textField isStretchWithOverflow="true" isBlankWhenNull="true">
				<reportElement style="Ячейка" stretchType="RelativeToBandHeight" x="145" y="15" width="20" height="20" uuid="d7394213-df75-4799-900b-c14998306aac"/>
				<textElement>
					<font isBold="true"/>
				</textElement>
				<textFieldExpression><![CDATA[$V{R1 & C1}]]></textFieldExpression>
			</textField>
 '''


template = bas_template.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}").replace('x="145"', 'x="{1}"')

template = re.sub(r'uuid=".+?"', 'uuid="{2}"', template)

all_gotovo = ""
i = 1
while i <= 31:
    x = 20 * i + 125
    gotovo = template.format(i, x, str(uuid.uuid4()),)
    all_gotovo = all_gotovo + gotovo + "\r\n"
    print(gotovo)
    i = i + 1

clipboard.copy(all_gotovo)



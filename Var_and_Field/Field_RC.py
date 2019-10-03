import clipboard
import uuid
import re

# --- ПОЛЕ ----------------------------------------------------------------------
field = '''
			<textField isStretchWithOverflow="true" isBlankWhenNull="true">
				<reportElement style="Ячейка" stretchType="RelativeToBandHeight" x="145" y="215" width="20" height="20" uuid="d7394213-df75-4799-900b-c14998306aac"/>
				<textElement>
					<font isBold="true"/>
				</textElement>
				<textFieldExpression><![CDATA[$V{R11 & C1}]]></textFieldExpression>
			</textField>
 '''


columnAndX = field.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}").replace('x="145"', 'x="{1}"')

columnAndX = re.sub(r'uuid=".+?"', 'uuid="{2}"', columnAndX)

allResult = ""

cx = 1
while cx <= 31:
    x = 20 * cx + 125
    columnAndXResult = columnAndX.format(cx, x, str(uuid.uuid4()),)
    allResult = allResult + columnAndXResult + "\r\n"
    print(columnAndXResult)
    cx = cx + 1

clipboard.copy(allResult)



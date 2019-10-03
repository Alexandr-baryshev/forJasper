import clipboard
import uuid
import re

# --- ПОЛЕ ----------------------------------------------------------------------
field = '''
			<textField isStretchWithOverflow="true" isBlankWhenNull="true">
				<reportElement style="Ячейка" stretchType="RelativeToBandHeight" x="145" y="20" width="20" height="20" uuid="d7394213-df75-4799-900b-c14998306aac"/>
				<textElement>
					<font isBold="true"/>
				</textElement>
				<textFieldExpression><![CDATA[$V{R1 & C1}]]></textFieldExpression>
			</textField>
 '''

allResult = ""
# --- R СТРОКА копипрование со сдвигом ry раз, где y = сдвиг по вертикали ---------------------------------->
rowAndY = field.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}").replace('y="20"', 'y="{1}"')
rowAndY = re.sub(r'uuid=".+?"', 'uuid="{2}"', rowAndY)
ry = 1
while ry <= 11:
    y = 20 * ry
    rowAndYResult = rowAndY.format(ry, y, str(uuid.uuid4()),)

    # --- C СТОЛБЕЦ копипрование со сдвигом cx раз, где x = сдвиг по горизонтали ----->
    columnAndX = rowAndYResult.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}").replace('x="145"', 'x="{1}"')
    columnAndX = re.sub(r'uuid=".+?"', 'uuid="{2}"', columnAndX)
    cx = 1
    while cx <= 31:
        x = 20 * cx + 125
        columnAndXResult = columnAndX.format(cx, x, str(uuid.uuid4()),)

        allResult = allResult + columnAndXResult + "\r\n"
        print(columnAndXResult)
        cx = cx + 1
        # --- СТОЛБЕЦ конец ------------------------------------------------------- ///


    ry = ry + 1

# --- СТРОКА конец ------------------------------------------------------------------------------------ ///

clipboard.copy(allResult)



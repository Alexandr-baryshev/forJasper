import clipboard
import uuid
import re

# --- ПОЛЕ ----------------------------------------------------------------------
field = '''
			<textField isBlankWhenNull="true">
				<reportElement style="Ячейка_C_root" x="570" y="15" width="50" height="15" uuid="37184b64-8621-4ceb-a68c-ffe56cc82c0b">
					<property name="com.jaspersoft.studio.unit.height" value="px"/>
					<property name="com.jaspersoft.studio.unit.width" value="px"/>
				</reportElement>
				<textFieldExpression><![CDATA[$V{R1 C10}]]></textFieldExpression>
			</textField>
 '''
# --- C СТОЛБЕЦ копипрование со сдвигом cx раз, где x = сдвиг по горизонтали ----->

# columnAndX = field.replace("{", "{{").replace("}", "}}").replace("1_", "{0}_").replace('x="120"', 'x="{1}"')
# columnAndX = re.sub(r'uuid=".+?"', 'uuid="{2}"', columnAndX)
#
# allResult = ""
#
# cx = 1
# while cx <= 8:
#     x = 50 * cx + 70
#     columnAndXResult = columnAndX.format(cx, x, str(uuid.uuid4()),)
#     allResult = allResult + columnAndXResult + "\r\n"
#     print(columnAndXResult)
#     cx = cx + 1
#
# clipboard.copy(allResult)

# --- СТОЛБЕЦ конец ---------------------------------------------------------- ///







# --- R СТРОКА копипрование со сдвигом ry раз, где y = сдвиг по вертикали ---------------------------------->

rowAndY = field.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}").replace('y="15"', 'y="{1}"')
rowAndY = re.sub(r'uuid=".+?"', 'uuid="{2}"', rowAndY)

allResult = ""

ry = 1
while ry <= 20:
    y = 15 * ry # - 30
    rowAndYResult = rowAndY.format(ry, y, str(uuid.uuid4()),)
    allResult = allResult + rowAndYResult + "\r\n"
    print(rowAndYResult)
    ry = ry + 1

clipboard.copy(allResult)

# --- СТРОКА конец -------------------------------------------------------------------------------------- ///


import clipboard
import uuid
import re

# --- ПОЛЕ ----------------------------------------------------------------------
field = '''
			<staticText>
				<reportElement style="Ячейка_L" x="0" y="0" width="170" height="30" uuid="d9855dda-dc75-46d4-9900-4eb87f083303">
					<property name="com.jaspersoft.studio.unit.height" value="px"/>
				</reportElement>
				<text><![CDATA[1]></text>
			</staticText>
 '''
# --- C СТОЛБЕЦ копипрование со сдвигом cx раз, где x = сдвиг по горизонтали ----->

columnAndX = field.replace("{", "{{").replace("}", "}}").replace("CDATA[1", "CDATA[{0}").replace('x="0"', 'x="{1}"')
columnAndX = re.sub(r'uuid=".+?"', 'uuid="{2}"', columnAndX)

allResult = ""

cx = 1
while cx <= 53:
    x = 30 * cx - 30
    columnAndXResult = columnAndX.format(cx, x, str(uuid.uuid4()),)
    allResult = allResult + columnAndXResult + "\r\n"
    print(columnAndXResult)
    cx = cx + 1

clipboard.copy(allResult)

# --- СТОЛБЕЦ конец ---------------------------------------------------------- ///







# --- R СТРОКА копипрование со сдвигом ry раз, где y = сдвиг по вертикали ---------------------------------->

# rowAndY = field.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}").replace('y="15"', 'y="{1}"')
# rowAndY = re.sub(r'uuid=".+?"', 'uuid="{2}"', rowAndY)
#
# allResult = ""
#
# ry = 1
# while ry <= 20:
#     y = 15 * ry # - 30
#     rowAndYResult = rowAndY.format(ry, y, str(uuid.uuid4()),)
#     allResult = allResult + rowAndYResult + "\r\n"
#     print(rowAndYResult)
#     ry = ry + 1
#
# clipboard.copy(allResult)

# --- СТРОКА конец -------------------------------------------------------------------------------------- ///


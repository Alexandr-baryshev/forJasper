import pyperclip
import uuid
import re

# --- ПОЛЕ ----------------------------------------------------------------------
field = '''
			<staticText>
				<reportElement style="Номер" stretchType="RelativeToBandHeight" x="0" y="0" width="20" height="20" uuid="6e537803-6378-4168-b716-f12419c86349">
					<property name="com.jaspersoft.studio.unit.width" value="px"/>
				</reportElement>
				<text><![CDATA[1]]></text>
			</staticText>
 '''
# --- C СТОЛБЕЦ копипрование со сдвигом cx раз, где x = сдвиг по горизонтали ----->

# columnAndX = field.replace("{", "{{").replace("}", "}}").replace("CDATA[1", "CDATA[{0}").replace('x="0"', 'x="{1}"')
# columnAndX = re.sub(r'uuid=".+?"', 'uuid="{2}"', columnAndX)
#
# allResult = ""
#
# cx = 1
# while cx <= 53:
#     x = 30 * cx - 30
#     columnAndXResult = columnAndX.format(cx, x, str(uuid.uuid4()),)
#     allResult = allResult + columnAndXResult + "\r\n"
#     print(columnAndXResult)
#     cx = cx + 1
#
# pyperclip.copy(allResult)

# --- СТОЛБЕЦ конец ---------------------------------------------------------- ///







# --- R СТРОКА копипрование со сдвигом ry раз, где y = сдвиг по вертикали ---------------------------------->

rowAndY = field.replace("{", "{{").replace("}", "}}").replace("CDATA[1", "CDATA[{0}").replace('y="0"', 'y="{1}"')
rowAndY = re.sub(r'uuid=".+?"', 'uuid="{2}"', rowAndY)

allResult = ""

ry = 1
while ry <= 33:
    y = 20 * ry - 20
    rowAndYResult = rowAndY.format(ry, y, str(uuid.uuid4()),)
    allResult = allResult + rowAndYResult + "\r\n"
    print(rowAndYResult)
    ry = ry + 1

pyperclip.copy(allResult)

# --- СТРОКА конец -------------------------------------------------------------------------------------- ///


import clipboard
import uuid
import re

# --- ПОЛЕ ----------------------------------------------------------------------
field = '''
			<textField isBlankWhenNull="true">
				<reportElement style="ЯчейкаГлав" stretchType="RelativeToBandHeight" x="145" y="240" width="20" height="20" uuid="f2620b24-14e8-4d01-a8f9-b8f7b61bbcb0"/>
				<textFieldExpression><![CDATA[$V{C1_sum}]]></textFieldExpression>
			</textField>
 '''
# --- C СТОЛБЕЦ копипрование со сдвигом cx раз, где x = сдвиг по горизонтали ----->

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

# --- СТОЛБЕЦ конец ------------------------------------------------------- ///







# --- R СТРОКА копипрование со сдвигом ry раз, где y = сдвиг по вертикали ---------------------------------->

# rowAndY = field.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}").replace('y="145"', 'y="{1}"')
# rowAndY = re.sub(r'uuid=".+?"', 'uuid="{2}"', rowAndY)
#
# allResult = ""
#
# ry = 1
# while ry <= 11:
#     y = 20 * ry
#     rowAndYResult = rowAndY.format(ry, y, str(uuid.uuid4()),)
#     allResult = allResult + rowAndYResult + "\r\n"
#     print(rowAndYResult)
#     ry = ry + 1
#
# clipboard.copy(allResult)


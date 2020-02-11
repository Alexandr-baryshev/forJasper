import clipboard
import uuid
import re

# --- ПОЛЕ ----------------------------------------------------------------------
field = '''
			<textField>
				<reportElement style="Ячейка_C_root" x="200" y="0" width="30" height="30" uuid="3038b4da-d37b-47f9-8513-44782bde815d">
					<property name="com.jaspersoft.studio.unit.height" value="px"/>
				</reportElement>
				<textFieldExpression><![CDATA[$V{R1 C3}]]></textFieldExpression>
			</textField>
 '''

allResult = ""
# --- R СТРОКА копипрование со сдвигом ry раз, где y = сдвиг по вертикали ---------------------------------->
rowAndY = field.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}").replace('y="0"', 'y="{1}"')
rowAndY = re.sub(r'uuid=".+?"', 'uuid="{2}"', rowAndY)
ry = 1
while ry <= 53:
    y = 30 * ry - 30
    rowAndYResult = rowAndY.format(ry, y, str(uuid.uuid4()),)

    # --- C СТОЛБЕЦ копипрование со сдвигом cx раз, где x = сдвиг по горизонтали ----->
    columnAndX = rowAndYResult.replace("{", "{{").replace("}", "}}").replace("C3", "C{0}").replace('x="200"', 'x="{1}"')
    columnAndX = re.sub(r'uuid=".+?"', 'uuid="{2}"', columnAndX)
    cx = 3
    while cx <= 19:
        x = 30 * cx + 110
        columnAndXResult = columnAndX.format(cx, x, str(uuid.uuid4()),)

        allResult = allResult + columnAndXResult + "\r\n"
        print(columnAndXResult)
        cx = cx + 1
        # --- СТОЛБЕЦ конец ------------------------------------------------------- ///


    ry = ry + 1

# --- СТРОКА конец ------------------------------------------------------------------------------------ ///

clipboard.copy(allResult)



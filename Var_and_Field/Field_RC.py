import clipboard
import uuid
import re

# --- ПОЛЕ ----------------------------------------------------------------------
field = '''
			<textField isBlankWhenNull="true">
				<reportElement style="Ячейка_C_root" x="420" y="15" width="50" height="15" uuid="bf775eea-fdea-4999-84ff-8d2947433685">
					<property name="com.jaspersoft.studio.unit.height" value="px"/>
					<property name="com.jaspersoft.studio.unit.width" value="px"/>
				</reportElement>
				<textFieldExpression><![CDATA[$V{R1 C7}]]></textFieldExpression>
			</textField>
 '''

allResult = ""
# --- R СТРОКА копипрование со сдвигом ry раз, где y = сдвиг по вертикали ---------------------------------->
rowAndY = field.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}").replace('y="15"', 'y="{1}"')
rowAndY = re.sub(r'uuid=".+?"', 'uuid="{2}"', rowAndY)
ry = 1
while ry <= 20:
    y = 15 * ry #+ 405
    rowAndYResult = rowAndY.format(ry, y, str(uuid.uuid4()),)

    # --- C СТОЛБЕЦ копипрование со сдвигом cx раз, где x = сдвиг по горизонтали ----->
    columnAndX = rowAndYResult.replace("{", "{{").replace("}", "}}").replace("C7", "C{0}").replace('x="420"', 'x="{1}"')
    columnAndX = re.sub(r'uuid=".+?"', 'uuid="{2}"', columnAndX)
    cx = 7
    while cx <= 8:
        x = 50 * cx + 70
        columnAndXResult = columnAndX.format(cx, x, str(uuid.uuid4()),)

        allResult = allResult + columnAndXResult + "\r\n"
        print(columnAndXResult)
        cx = cx + 1
        # --- СТОЛБЕЦ конец ------------------------------------------------------- ///


    ry = ry + 1

# --- СТРОКА конец ------------------------------------------------------------------------------------ ///

clipboard.copy(allResult)



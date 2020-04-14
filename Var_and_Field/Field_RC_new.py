import pyperclip
import uuid
import re

from colorama import Fore, Back, Style

# --- ПОЛЕ ----------------------------------------------------------------------
'''
	<textField>
		<reportElement style="Ячейка_C_root" x="160" y="0" width="40" height="20" uuid="9308e085-69d6-4695-9806-00d4715e69c9"/>
		<textFieldExpression><![CDATA[$V{R1 C1}]]></textFieldExpression>
	</textField>
 '''


# --- R СТРОКА копипрование со сдвигом ry раз, где y = сдвиг по вертикали ---------------------------------->

def Field(field, R_Start, R_Size, C_Start, C_Size):
    allResult = ""
    rowAndY = field.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}").replace('y="0"', 'y="{1}"')
    rowAndY = re.sub(r'uuid=".+?"', 'uuid="{2}"', rowAndY)
    ry = R_Start
    while ry <= R_Size:
        y = 20 * ry - 20
        rowAndYResult = rowAndY.format(ry, y, str(uuid.uuid4()), )

        # --- C СТОЛБЕЦ копипрование со сдвигом cx раз, где x = сдвиг по горизонтали ----->
        columnAndX = rowAndYResult.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}").replace('x="160"', 'x="{1}"')
        columnAndX = re.sub(r'uuid=".+?"', 'uuid="{2}"', columnAndX)
        cx = C_Start
        while cx <= C_Size:
            x = 40 * cx + 120
            columnAndXResult = columnAndX.format(cx, x, str(uuid.uuid4()), )

            allResult = allResult + columnAndXResult + "\r\n"
            print(Fore.GREEN + columnAndXResult)
            cx = cx + 1
            # --- СТОЛБЕЦ конец ------------------------------------------------------- ///

        ry = ry + 1
    pyperclip.copy(allResult)
    return allResult

# --- СТРОКА конец ------------------------------------------------------------------------------------ ///



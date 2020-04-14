import pyperclip
from tkinter import *
from colorama import Fore

# Образец переменной
'''
	<variable name="R1 C1" class="java.lang.Integer" calculation="DistinctCount">
		<variableExpression><![CDATA[$V{R1} && $V{C1} ? $F{Идентификатор происшествия} : null]]></variableExpression>
	</variable>
'''

variable: str

# Приоритет колонки
def Cx_Rx(R_Start, R_Size, C_Start, C_Size):
    allResult = ""
    row = variable.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}")
    c = C_Start
    while c <= C_Size:
        rowResult = row.format(c)

        # --- R СТРОКА замена X раз ->
        column = rowResult.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}")
        r = R_Start
        while r <= R_Size:
            columnResult = column.format(r)
            allResult = allResult + columnResult + "\r\n"
            # print(columnResult)
            r = r + 1
        # --- СТОЛБЕЦ конец - ///

        c = c + 1
    pyperclip.copy(allResult)
    return allResult


# Приоритет строки
def Rx_Cx(R_Start, R_Size, C_Start, C_Size):
    allResult = ""
    row = variable.replace("{", "{{").replace("}", "}}").replace("R1", "R{0}")
    r = R_Start
    while r <= R_Size:
        rowResult = row.format(r)

        # --- R СТРОКА замена X раз ->
        column = rowResult.replace("{", "{{").replace("}", "}}").replace("C1", "C{0}")
        c = C_Start
        while c <= C_Size:
            columnResult = column.format(c)
            allResult = allResult + columnResult + "\r\n"
            c = c + 1
        # --- СТОЛБЕЦ конец - ///

        r = r + 1
    pyperclip.copy(allResult)
    return allResult


# Цикл выбора приоритета
# prioritet = ""
# while prioritet != "c" or prioritet != "r":
#     if prioritet == "c":
#         Cx_Rx()
#     if prioritet == "r":
#         Rx_Cx()

# ================ GUI =============================
root = Tk()
root.title("Генератор переменных")

entry1 = Entry(root, width=10, font=15)
entry2 = Entry(root, width=10, font=15)
entry3 = Entry(root, width=10, font=15)
entry4 = Entry(root, width=10, font=15)

button1 = Button(root, text="Генерировать")
label1 = Label(root, width=20, font=15)

entry1.grid(row=0, column=0)
entry2.grid(row=0, column=1)
entry3.grid(row=0, column=2)
entry4.grid(row=0, column=3)

button1.grid(row=0, column=4)
label1.grid(row=0, column=5)


def output(event):
    p1 = entry1.get()
    p2 = entry2.get()
    p3 = entry3.get()
    p4 = entry4.get()
    Rx_Cx(int(p1), int(p2), int(p3), int(p4))



button1.bind("<Button-1>", output)

root.mainloop()

import pyperclip
from tkinter import *
from tkinter import ttk
from colorama import Fore

# Образец переменной
'''
	<variable name="R1 C1" class="java.lang.Integer" calculation="DistinctCount">
		<variableExpression><![CDATA[$V{R1} && $V{C1} ? $F{Идентификатор происшествия} : null]]></variableExpression>
	</variable>
'''


# Приоритет колонки
def Cx_Rx(variable, R_Start, R_Size, C_Start, C_Size):
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
def Rx_Cx(variable, R_Start, R_Size, C_Start, C_Size):
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


# ================ GUI =============================

root = Tk()
root.title("Генератор переменных")

R_Start = Entry(root, width=10, font=3)
R_Start.insert(END, 'Начало строки')

R_Size = Entry(root, width=10, font=10)
R_Size.insert(END, 'Размер строки')

C_Start = Entry(root, width=10, font=10)
C_Start.insert(END, 'Начало колонки')

C_Size = Entry(root, width=10, font=10)
C_Size.insert(END, 'Размер колонки')

prioritet = Entry(root, width=10, font=10, bg="red")
prioritet.insert(END, 'Приоритет R / C')

textInput = Text(root, bg="#c4dbed")

buttonGen = Button(root, text="Генерировать")
textOut = Text(root, bg="#c4dbed")

R_Start.grid(row=0, column=0)
R_Size.grid(row=0, column=1)
C_Start.grid(row=0, column=2)
C_Size.grid(row=0, column=3)
prioritet.grid(row=0, column=4)

buttonGen.grid(row=0, column=5)
textInput.grid(row=1, column=0, columnspan=6, sticky="nsew")
textOut.grid(row=2, column=0, columnspan=6, sticky="nsew")


def output(event):
    textOut.delete(1.0, END)
    if prioritet.get() == "c":
        textOut.insert(1.0, Cx_Rx(textInput.get(1.0, END), int(R_Start.get()), int(R_Size.get()), int(C_Start.get()), int(C_Size.get())))
    if prioritet.get() == "r":
        textOut.insert(1.0, Rx_Cx(textInput.get(1.0, END), int(R_Start.get()), int(R_Size.get()), int(C_Start.get()), int(C_Size.get())))


buttonGen.bind("<Button-1>", output)


# Конфигурация
root.columnconfigure(4, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=2)

root.mainloop()

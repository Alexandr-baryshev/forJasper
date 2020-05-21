import pyperclip
from tkinter import *

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

p1 = Label(root, width=15, text="Начало строки")
p1.grid(row=0, column=0)
R_Start = Entry(root, width=15)
R_Start.grid(row=1, column=0)

p2 = Label(root, width=15, text="Размер строки")
p2.grid(row=0, column=1)
R_Size = Entry(root, width=15)
R_Size.grid(row=1, column=1)

p3 = Label(root, width=15, text="Начало колонки")
p3.grid(row=0, column=2)
C_Start = Entry(root, width=15)
C_Start.grid(row=1, column=2)

p4 = Label(root, width=15, text="Размер строки")
p4.grid(row=0, column=3)
C_Size = Entry(root, width=15)
C_Size.grid(row=1, column=3)

p5 = Label(root, width=15, text="Приоритет R / C")
p5.grid(row=0, column=4)
prioritet = Entry(root, width=15, bg="#f5ebc6")
prioritet.grid(row=1, column=4)

buttonGen = Button(root, text="Генерировать", bg="#ffd7a3")
buttonGen.grid(row=0, column=5, rowspan=2, sticky="nse")

textInput = Text(root, bg="#f3ffe8")
textInput.grid(row=2, column=0, columnspan=6, sticky="nsew")

textOut = Text(root, bg="#c4dbed")
textOut.grid(row=3, column=0, columnspan=6, sticky="nsew")


def output(event):
    textOut.delete(1.0, END)
    if prioritet.get() == "c":
        textOut.insert(1.0, Cx_Rx(textInput.get(1.0, END), int(R_Start.get()), int(R_Size.get()), int(C_Start.get()),
                                  int(C_Size.get())))
    if prioritet.get() == "r":
        textOut.insert(1.0, Rx_Cx(textInput.get(1.0, END), int(R_Start.get()), int(R_Size.get()), int(C_Start.get()),
                                  int(C_Size.get())))


buttonGen.bind("<Button-1>", output)

# Конфигурация
root.columnconfigure(5, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=2)

root.mainloop()

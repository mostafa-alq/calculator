import tkinter as tk

#functions
def addition(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate():
    global calculation
    try:
        calculation = eval(calculation)
        calculation = str(round(calculation, 3))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear()
        text_result.insert(1.0, "Error!")    
        pass

def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

#setting it up

compiler = tk.Tk()
compiler.title('HalalCalculator')
compiler.iconbitmap("kaaba2.ico")
compiler.geometry("260x275")

calculation = ""


#Main screen

text_result = tk.Text(compiler, height=2, width=14, font=('Arial', 24))
text_result.grid(columnspan=15)

#buttons

#row 1
btn_1 = tk.Button(compiler, text='1', command = lambda:addition(1), width = 5, font=('Arial', 14))
btn_1.grid(row=2,column=1)

btn_2 = tk.Button(compiler, text='2', command = lambda:addition(2), width = 5, font=('Arial', 14))
btn_2.grid(row=2,column=2)

btn_3 = tk.Button(compiler, text='3', command = lambda:addition(3), width = 5, font=('Arial', 14))
btn_3.grid(row=2,column=3)

btn_plus = tk.Button(compiler, text='+', command = lambda:addition("+"), width = 5, font=('Arial', 14))
btn_plus.grid(row=2,column=4)

#row 2
btn_4 = tk.Button(compiler, text='4', command = lambda:addition(4), width = 5, font=('Arial', 14))
btn_4.grid(row=3,column=1)

btn_5 = tk.Button(compiler, text='5', command = lambda:addition(5), width = 5, font=('Arial', 14))
btn_5.grid(row=3,column=2)

btn_6 = tk.Button(compiler, text='6', command = lambda:addition(6), width = 5, font=('Arial', 14))
btn_6.grid(row=3,column=3)

btn_minus = tk.Button(compiler, text='-', command = lambda:addition("-"), width = 5, font=('Arial', 14))
btn_minus.grid(row=3,column=4)

#row 3
btn_7 = tk.Button(compiler, text='7', command = lambda:addition(7), width = 5, font=('Arial', 14))
btn_7.grid(row=4,column=1)

btn_8 = tk.Button(compiler, text='8', command = lambda:addition(8), width = 5, font=('Arial', 14))
btn_8.grid(row=4,column=2)

btn_9 = tk.Button(compiler, text='9', command = lambda:addition(9), width = 5, font=('Arial', 14))
btn_9.grid(row=4,column=3)

btn_mult = tk.Button(compiler, text='*', command = lambda:addition("*"), width = 5, font=('Arial', 14))
btn_mult.grid(row=4,column=4)

#row 4
btn_par1 = tk.Button(compiler, text='(', command = lambda:addition("("), width = 5, font=('Arial', 14))
btn_par1.grid(row=5,column=1)

btn_0 = tk.Button(compiler, text='0', command = lambda:addition(0), width = 5, font=('Arial', 14))
btn_0.grid(row=5,column=2)

btn_par2 = tk.Button(compiler, text=')', command = lambda:addition(')'), width = 5, font=('Arial', 14))
btn_par2.grid(row=5,column=3)

btn_div = tk.Button(compiler, text='/', command = lambda:addition("/"), width = 5, font=('Arial', 14))
btn_div.grid(row=5,column=4)

#row 5
btn_clear = tk.Button(compiler, text='C', command = clear, width = 11, font=('Arial', 14))
btn_clear.grid(row=6,column=1,columnspan=2)

btn_equals = tk.Button(compiler, text='=', command = evaluate, width = 11, font=('Arial', 14))
btn_equals.grid(row=6,column=3,columnspan=2)

compiler.mainloop()
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

root = tk.Tk()
root.title("آلة حاسبة")

entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0

for button in buttons:
    btn = tk.Button(root, text=button, padx=10, pady=5, font=("Arial", 12), command=lambda btn=button: button_click(btn))
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

btn_clear = tk.Button(root, text="Clear", padx=10, pady=5, font=("Arial", 12), command=button_clear)
btn_clear.grid(row=row, column=col, padx=5, pady=5)

btn_equal = tk.Button(root, text="=", padx=10, pady=5, font=("Arial", 12), command=button_equal)
btn_equal.grid(row=row, column=col+1, padx=5, pady=5)

root.mainloop()

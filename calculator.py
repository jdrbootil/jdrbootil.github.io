import math
import tkinter as tk

root = tk.Tk()
root.title("Python Calculator for OOP")
root.geometry("310x420")
root.resizable(False, False)

first_num = 0.0
operator = ""
is_typing_second_num = False


def press_num(num):
  global is_typing_second_num
  if is_typing_second_num:
    equation.set("")
    is_typing_second_num = False

  current = equation.get()
  equation.set(current + str(num))


def press_operator(op):
  global first_num, operator, is_typing_second_num
  try:
    first_num = float(equation.get())
    operator = op
    is_typing_second_num = True
  except ValueError:
    equation.set("Error")


def equal_press():
  global first_num, operator
  try:
    second_num = float(equation.get())
    result = 0.0

    if operator == "+":
      result = first_num + second_num
    elif operator == "-":
      result = first_num - second_num
    elif operator == "*":
      result = first_num * second_num
    elif operator == "/":
      if second_num == 0:
        equation.set("Error: Div by 0")
        return
      else:
        result = first_num / second_num
    else:
      return
    
    if result.is_integer():
      equation.set(int(result))
    else:
      equation.set(round(result, 4))

  except ValueError:
    equation.set("Error")


def clear():
  global first_num, operator, is_typing_second_num
  first_num = 0.0
  operator = ""
  is_typing_second_num = False
  equation.set("")

def square_root():
  try:
    val = float(equation.get())
    if val < 0:
      equation.set("Error: Negative √")
    else:
      res = math.sqrt(val)
      equation.set(int(res) if res.is_integer() else round(res, 4))
  except ValueError:
    equation.set("Error")


def power_of_two():
  try:
    val = float(equation.get())
    res = val**2
    equation.set(int(res) if res.is_integer() else round(res, 4))
  except ValueError:
    equation.set("Error")


equation = tk.StringVar()

entry_field = tk.Entry(
    root,
    font=("arial", 18, "bold"),
    textvariable=equation,
    width=19,
    bg="#eee",
    bd=5,
    justify="right",
)
entry_field.pack(ipady=10, pady=10)

btns_frame = tk.Frame(root, bg="lightgray")
btns_frame.pack()

tk.Button(
    btns_frame,
    text="C",
    width=6,
    height=2,
    bg="#f05454",
    fg="white",
    command=clear,
).grid(row=0, column=0, padx=2, pady=2)
tk.Button(
    btns_frame,
    text="√",
    width=6,
    height=2,
    bg="#30475e",
    fg="white",
    command=square_root,
).grid(row=0, column=1, padx=2, pady=2)
tk.Button(
    btns_frame,
    text="x²",
    width=6,
    height=2,
    bg="#30475e",
    fg="white",
    command=power_of_two,
).grid(row=0, column=2, padx=2, pady=2)
tk.Button(
    btns_frame,
    text="/",
    width=6,
    height=2,
    bg="#f2a365",
    command=lambda: press_operator("/"),
).grid(row=0, column=3, padx=2, pady=2)

tk.Button(
    btns_frame, text="7", width=6, height=2, command=lambda: press_num(7)
).grid(row=1, column=0, padx=2, pady=2)
tk.Button(
    btns_frame, text="8", width=6, height=2, command=lambda: press_num(8)
).grid(row=1, column=1, padx=2, pady=2)
tk.Button(
    btns_frame, text="9", width=6, height=2, command=lambda: press_num(9)
).grid(row=1, column=2, padx=2, pady=2)
tk.Button(
    btns_frame,
    text="*",
    width=6,
    height=2,
    bg="#f2a365",
    command=lambda: press_operator("*"),
).grid(row=1, column=3, padx=2, pady=2)

tk.Button(
    btns_frame, text="4", width=6, height=2, command=lambda: press_num(4)
).grid(row=2, column=0, padx=2, pady=2)
tk.Button(
    btns_frame, text="5", width=6, height=2, command=lambda: press_num(5)
).grid(row=2, column=1, padx=2, pady=2)
tk.Button(
    btns_frame, text="6", width=6, height=2, command=lambda: press_num(6)
).grid(row=2, column=2, padx=2, pady=2)
tk.Button(
    btns_frame,
    text="-",
    width=6,
    height=2,
    bg="#f2a365",
    command=lambda: press_operator("-"),
).grid(row=2, column=3, padx=2, pady=2)

tk.Button(
    btns_frame, text="1", width=6, height=2, command=lambda: press_num(1)
).grid(row=3, column=0, padx=2, pady=2)
tk.Button(
    btns_frame, text="2", width=6, height=2, command=lambda: press_num(2)
).grid(row=3, column=1, padx=2, pady=2)
tk.Button(
    btns_frame, text="3", width=6, height=2, command=lambda: press_num(3)
).grid(row=3, column=2, padx=2, pady=2)
tk.Button(
    btns_frame,
    text="+",
    width=6,
    height=2,
    bg="#f2a365",
    command=lambda: press_operator("+"),
).grid(row=3, column=3, padx=2, pady=2)

tk.Button(
    btns_frame, text="0", width=14, height=2, command=lambda: press_num(0)
).grid(row=4, column=0, columnspan=2, padx=2, pady=2)
tk.Button(
    btns_frame, text=".", width=6, height=2, command=lambda: press_num(".")
).grid(row=4, column=2, padx=2, pady=2)
tk.Button(
    btns_frame,
    text="=",
    width=6,
    height=2,
    bg="#228b22",
    fg="white",
    command=equal_press,
).grid(row=4, column=3, padx=2, pady=2)

root.mainloop()

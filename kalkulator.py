import tkinter as tk
from tkinter import messagebox
import math

# ===== KOLORY =====
COLOR_BG = "#1a1a2e"
COLOR_FRAME = "#16213e"
COLOR_BUTTON = "#0f3460"
COLOR_BUTTON_HOVER = "#1a5276"
COLOR_ACCENT = "#e94560"
COLOR_TEXT = "#ffffff"
COLOR_TEXT_SECONDARY = "#a0a0b0"
COLOR_RESULT = "#4ecca3"
COLOR_ENTRY_BG = "#0d1b2a"
COLOR_ENTRY_FG = "#ffffff"

current_op = None
first_num = None
second_num = None
reset_screen = False

def update_display(value):
    entry_display.delete(0, tk.END)
    entry_display.insert(0, value)

def click_number(num):
    global reset_screen
    current = entry_display.get()
    if reset_screen:
        update_display(str(num))
        reset_screen = False
    else:
        if current == "0" and num != ".":
            update_display(str(num))
        else:
            update_display(current + str(num))

def click_operator(op):
    global first_num, current_op, reset_screen
    try:
        first_num = float(entry_display.get())
        current_op = op
        reset_screen = True
        label_operation.config(text=f"{first_num} {op}")
    except ValueError:
        pass

def click_equals():
    global first_num, current_op, reset_screen
    try:
        second_num = float(entry_display.get())
        result = None

        if current_op == "+":
            result = first_num + second_num
        elif current_op == "-":
            result = first_num - second_num
        elif current_op == "×":
            result = first_num * second_num
        elif current_op == "÷":
            if second_num == 0:
                raise ZeroDivisionError
            result = first_num / second_num
        elif current_op == "^":
            result = first_num ** second_num

        if result is not None:
            if result == int(result):
                result = int(result)
            update_display(str(result))
            label_operation.config(text=f"{first_num} {current_op} {second_num} =")
            first_num = result
            reset_screen = True
        else:
            update_display("Błąd")
    except ZeroDivisionError:
        update_display("Dziel. przez 0!")
        label_operation.config(text="BŁĄD")
    except (ValueError, OverflowError):
        update_display("Błąd")
        label_operation.config(text="BŁĄD")

def click_clear():
    global first_num, current_op, reset_screen
    first_num = None
    current_op = None
    reset_screen = False
    update_display("0")
    label_operation.config(text="")

def click_backspace():
    current = entry_display.get()
    if len(current) > 1 and current != "0":
        update_display(current[:-1])
    else:
        update_display("0")

def click_percent():
    try:
        val = float(entry_display.get())
        update_display(str(val / 100))
    except ValueError:
        pass

def click_sqrt():
    try:
        val = float(entry_display.get())
        if val < 0:
            update_display("Błąd")
            return
        result = math.sqrt(val)
        if result == int(result):
            result = int(result)
        update_display(str(result))
    except ValueError:
        pass

def click_plus_minus():
    try:
        val = float(entry_display.get())
        update_display(str(-val))
    except ValueError:
        pass

def on_button_enter(e):
    e.widget.config(bg=COLOR_BUTTON_HOVER)

def on_button_leave(e):
    e.widget.config(bg=COLOR_BUTTON)

def on_accent_enter(e):
    e.widget.config(bg=COLOR_ACCENT)

def on_accent_leave(e):
    e.widget.config(bg=COLOR_ACCENT)

def key_handler(event):
    key = event.char
    if key.isdigit() or key == ".":
        click_number(key)
    elif key == "+":
        click_operator("+")
    elif key == "-":
        click_operator("-")
    elif key == "*":
        click_operator("×")
    elif key == "/":
        click_operator("÷")
    elif key == "^":
        click_operator("^")
    elif key == "\r" or key == "=":
        click_equals()
    elif key == "\x08":  # Backspace
        click_backspace()
    elif key == "\x1b":  # Escape
        click_clear()

# ===== GUI =====
root = tk.Tk()
root.title("Kalkulator")
root.geometry("340x500")
root.resizable(False, False)
root.configure(bg=COLOR_BG)
root.bind("<Key>", key_handler)

# === WYŚWIETLACZ ===
display_frame = tk.Frame(root, bg=COLOR_BG)
display_frame.pack(fill="x", padx=15, pady=(20, 5))

label_operation = tk.Label(display_frame, text="", font=("Segoe UI", 11),
                           bg=COLOR_BG, fg=COLOR_TEXT_SECONDARY, anchor="e")
label_operation.pack(fill="x", pady=(0, 2))

entry_display = tk.Entry(display_frame, font=("Segoe UI", 26, "bold"),
                         bg=COLOR_ENTRY_BG, fg=COLOR_ENTRY_FG,
                         bd=0, relief="flat", justify="right",
                         highlightthickness=0)
entry_display.pack(fill="x", ipady=12)
entry_display.insert(0, "0")

# === PRZYCISKI ===
btn_frame = tk.Frame(root, bg=COLOR_BG)
btn_frame.pack(fill="both", expand=True, padx=12, pady=(10, 15))

# Konfiguracja siatki
for i in range(4):
    btn_frame.grid_columnconfigure(i, weight=1, uniform="col")

# (wiersz, kolumna, tekst, komenda, kolor_tła, colspan)
buttons = [
    # Wiersz 0
    ("C", click_clear, COLOR_ACCENT, 1, 0),
    ("⌫", click_backspace, COLOR_BUTTON, 1, 1),
    ("%", click_percent, COLOR_BUTTON, 1, 2),
    ("÷", lambda: click_operator("÷"), COLOR_BUTTON, 1, 3),
    # Wiersz 1
    ("7", lambda: click_number("7"), COLOR_BUTTON, 1, 0),
    ("8", lambda: click_number("8"), COLOR_BUTTON, 1, 1),
    ("9", lambda: click_number("9"), COLOR_BUTTON, 1, 2),
    ("×", lambda: click_operator("×"), COLOR_BUTTON, 1, 3),
    # Wiersz 2
    ("4", lambda: click_number("4"), COLOR_BUTTON, 1, 0),
    ("5", lambda: click_number("5"), COLOR_BUTTON, 1, 1),
    ("6", lambda: click_number("6"), COLOR_BUTTON, 1, 2),
    ("-", lambda: click_operator("-"), COLOR_BUTTON, 1, 3),
    # Wiersz 3
    ("1", lambda: click_number("1"), COLOR_BUTTON, 1, 0),
    ("2", lambda: click_number("2"), COLOR_BUTTON, 1, 1),
    ("3", lambda: click_number("3"), COLOR_BUTTON, 1, 2),
    ("+", lambda: click_operator("+"), COLOR_BUTTON, 1, 3),
    # Wiersz 4
    ("±", click_plus_minus, COLOR_BUTTON, 1, 0),
    ("0", lambda: click_number("0"), COLOR_BUTTON, 1, 1),
    (".", lambda: click_number("."), COLOR_BUTTON, 1, 2),
    ("=", click_equals, COLOR_RESULT, 1, 3),
]

# Dodaj przyciski z potęgowaniem w dodatkowym wierszu
extra_buttons = [
    ("^", lambda: click_operator("^"), COLOR_BUTTON, 1, 0),
    ("√", click_sqrt, COLOR_BUTTON, 1, 1),
]

for btn in buttons:
    text, cmd, color, colspan, row = btn
    b = tk.Button(btn_frame, text=text, font=("Segoe UI", 14, "bold"),
                  bg=color, fg=COLOR_TEXT, bd=0, padx=5, pady=8,
                  activebackground=color, activeforeground=COLOR_TEXT,
                  cursor="hand2", command=cmd)
    b.grid(row=row, column=colspan, padx=2, pady=2, sticky="nsew")

# Dodaj przyciski ^ i √ w osobnej ramce poniżej
extra_frame = tk.Frame(root, bg=COLOR_BG)
extra_frame.pack(fill="x", padx=12, pady=(0, 15))
for i in range(4):
    extra_frame.grid_columnconfigure(i, weight=1, uniform="col")

for text, cmd, color, *pos in extra_buttons:
    b = tk.Button(extra_frame, text=text, font=("Segoe UI", 12, "bold"),
                  bg=color, fg=COLOR_TEXT, bd=0, padx=5, pady=6,
                  activebackground=color, activeforeground=COLOR_TEXT,
                  cursor="hand2", command=cmd)
    b.grid(row=0, column=pos[1] if pos else 0, padx=2, pady=2, sticky="nsew")

# Stopka
tk.Label(root, text="⌨️ Klawiatura: cyfry, +-*/, Enter=, Esc=C, Backspace",
         font=("Segoe UI", 7), bg=COLOR_BG, fg=COLOR_TEXT_SECONDARY).pack(pady=(0, 8))

root.mainloop()

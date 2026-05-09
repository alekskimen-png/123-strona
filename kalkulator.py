import tkinter as tk
from tkinter import messagebox
import math

# ===== KOLORY (ciemny motyw) =====
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
    entry_display.insert(tk.END, value)

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
        update_display("Błąd")

def click_square():
    try:
        val = float(entry_display.get())
        result = val ** 2
        if result == int(result):
            result = int(result)
        update_display(str(result))
    except ValueError:
        update_display("Błąd")

def click_toggle_sign():
    try:
        val = float(entry_display.get())
        update_display(str(-val))
    except ValueError:
        pass

def click_power():
    global first_num, current_op, reset_screen
    try:
        first_num = float(entry_display.get())
        current_op = "^"
        reset_screen = True
        label_operation.config(text=f"{first_num} ^")
    except ValueError:
        pass

def on_enter(e, btn):
    btn.config(bg=COLOR_BUTTON_HOVER)

def on_leave(e, btn):
    bg = btn.cget("bg")
    if bg != COLOR_ACCENT:
        btn.config(bg=COLOR_BUTTON)

# ===== GŁÓWNE OKNO =====
root = tk.Tk()
root.title("Kalkulator")
root.geometry("380x560")
root.resizable(False, False)
root.configure(bg=COLOR_BG)
root.eval("tk::PlaceWindow . center")

# ===== STYL =====
style = {
    "bg": COLOR_BUTTON,
    "fg": COLOR_TEXT,
    "font": ("Segoe UI", 14, "bold"),
    "relief": "flat",
    "bd": 0,
    "activebackground": COLOR_BUTTON_HOVER,
    "activeforeground": COLOR_TEXT,
    "cursor": "hand2",
}

style_op = {
    **style,
    "bg": COLOR_ACCENT,
    "activebackground": "#c0392b",
}

style_func = {
    **style,
    "bg": "#0d7377",
    "activebackground": "#0a5c5e",
}

# ===== NAGŁÓWEK =====
header = tk.Frame(root, bg=COLOR_BG)
header.pack(fill="x", padx=20, pady=(15, 5))

tk.Label(header, text="⚡ KALKULATOR", font=("Segoe UI", 18, "bold"),
         bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor="w")

tk.Label(header, text="nowoczesny kalkulator naukowy", font=("Segoe UI", 9),
         bg=COLOR_BG, fg=COLOR_TEXT_SECONDARY).pack(anchor="w")

# ===== WYŚWIETLACZ =====
display_frame = tk.Frame(root, bg=COLOR_BG, padx=20, pady=(5, 0))
display_frame.pack(fill="x")

# Etykieta operacji
label_operation = tk.Label(display_frame, text="", font=("Segoe UI", 11),
                           bg=COLOR_FRAME, fg=COLOR_TEXT_SECONDARY, anchor="e",
                           height=1, padx=15)
label_operation.pack(fill="x", padx=0, pady=0)
label_operation.config(bg=COLOR_FRAME)

# Pole wyświetlacza
entry_display = tk.Entry(display_frame, font=("Segoe UI", 28, "bold"),
                         bg=COLOR_ENTRY_BG, fg=COLOR_TEXT, insertbackground=COLOR_ACCENT,
                         relief="flat", bd=0, justify="right", padx=15)
entry_display.pack(fill="x", ipady=12, pady=(0, 0))
entry_display.insert(0, "0")

# ===== PRZYCISKI =====
button_frame = tk.Frame(root, bg=COLOR_BG, padx=15, pady=10)
button_frame.pack(fill="both", expand=True)

buttons = [
    # [tekst, komenda, styl, colspan]
    ["C", click_clear, style_func, 1],
    ["⌫", click_backspace, style_func, 1],
    ["%", click_percent, style_func, 1],
    ["÷", lambda: click_operator("÷"), style_op, 1],
    ["7", lambda: click_number(7), style, 1],
    ["8", lambda: click_number(8), style, 1],
    ["9", lambda: click_number(9), style, 1],
    ["×", lambda: click_operator("×"), style_op, 1],
    ["4", lambda: click_number(4), style, 1],
    ["5", lambda: click_number(5), style, 1],
    ["6", lambda: click_number(6), style, 1],
    ["−", lambda: click_operator("-"), style_op, 1],
    ["1", lambda: click_number(1), style, 1],
    ["2", lambda: click_number(2), style, 1],
    ["3", lambda: click_number(3), style, 1],
    ["+", lambda: click_operator("+"), style_op, 1],
    ["±", click_toggle_sign, style_func, 1],
    ["0", lambda: click_number(0), style, 1],
    [".", lambda: click_number("."), style, 1],
    ["=", click_equals, style_op, 1],
]

# Dodatkowe przyciski naukowe
science_buttons = [
    ["√x", click_sqrt, style_func],
    ["x²", click_square, style_func],
    ["x^y", click_power, style_func],
]

# Ramka na przyciski naukowe
science_frame = tk.Frame(button_frame, bg=COLOR_BG)
science_frame.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 8))
for i, (txt, cmd, stl) in enumerate(science_buttons):
    btn = tk.Button(science_frame, text=txt, command=cmd, **stl)
    btn.pack(side="left", fill="x", expand=True, padx=2, ipady=6)
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

# Główna siatka przycisków
for idx, (text, command, btn_style, colspan) in enumerate(buttons):
    row = (idx // 4) + 1
    col = idx % 4

    btn = tk.Button(button_frame, text=text, command=command, **btn_style)

    if text == "=":
        btn.config(bg="#e94560")
    elif text == "C":
        btn.config(bg="#c0392b")
    elif text == "⌫":
        btn.config(bg="#7f8c8d")
    elif text == "0":
        btn.config(bg="#1a5276")

    btn.grid(row=row, column=col, columnspan=colspan,
             sticky="nsew", padx=3, pady=3, ipady=12)

    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

# Konfiguracja wag kolumn
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1, uniform="btn")

# ===== SKRÓTY KLAWISZOWE =====
root.bind("<Return>", lambda e: click_equals())
root.bind("<BackSpace>", lambda e: click_backspace())
root.bind("<Escape>", lambda e: click_clear())
root.bind("<c>", lambda e: click_clear())
root.bind("<plus>", lambda e: click_operator("+"))
root.bind("<minus>", lambda e: click_operator("-"))
root.bind("<asterisk>", lambda e: click_operator("×"))
root.bind("<slash>", lambda e: click_operator("÷"))
root.bind("^", lambda e: click_power())

for i in range(10):
    root.bind(str(i), lambda e, n=i: click_number(n))
root.bind("<period>", lambda e: click_number("."))

# ===== STOPKA =====
footer = tk.Frame(root, bg=COLOR_BG)
footer.pack(fill="x", padx=20, pady=(0, 10))
tk.Label(footer, text="🧮 klawiatura: cyfry + Enter · Esc · Backspace",
         font=("Segoe UI", 8), bg=COLOR_BG, fg=COLOR_TEXT_SECONDARY).pack()

# ===== URUCHOMIENIE =====
root.mainloop()

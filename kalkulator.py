import tkinter as tk
from tkinter import messagebox

def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b == 0:
        return "Nie można dzielić przez zero!"
    return a / b

def wykonaj_dzialanie(dzialanie):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        if dzialanie == "+":
            wynik = dodaj(a, b)
        elif dzialanie == "-":
            wynik = odejmij(a, b)
        elif dzialanie == "*":
            wynik = pomnoz(a, b)
        elif dzialanie == "/":
            wynik = podziel(a, b)

        label_wynik.config(text=f"Wynik: {wynik}")
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawne liczby!")

# GUI
root = tk.Tk()
root.title("Kalkulator")
root.geometry("320x280")
root.resizable(False, False)

tk.Label(root, text="Kalkulator", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Pierwsza liczba:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_a = tk.Entry(frame, width=15)
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Druga liczba:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_b = tk.Entry(frame, width=15)
entry_b.grid(row=1, column=1, padx=5, pady=5)

frame_przyciski = tk.Frame(root)
frame_przyciski.pack(pady=10)

tk.Button(frame_przyciski, text="+", width=5, font=("Arial", 12),
          command=lambda: wykonaj_dzialanie("+")).grid(row=0, column=0, padx=5)
tk.Button(frame_przyciski, text="-", width=5, font=("Arial", 12),
          command=lambda: wykonaj_dzialanie("-")).grid(row=0, column=1, padx=5)
tk.Button(frame_przyciski, text="*", width=5, font=("Arial", 12),
          command=lambda: wykonaj_dzialanie("*")).grid(row=0, column=2, padx=5)
tk.Button(frame_przyciski, text="/", width=5, font=("Arial", 12),
          command=lambda: wykonaj_dzialanie("/")).grid(row=0, column=3, padx=5)

label_wynik = tk.Label(root, text="Wynik: —", font=("Arial", 14, "bold"), fg="green")
label_wynik.pack(pady=15)

tk.Button(root, text="Wyjdź", command=root.destroy, bg="#e74c3c", fg="white", width=10).pack(pady=5)

root.mainloop()

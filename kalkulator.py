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

def main():
    print("=== PROSTY KALKULATOR ===")
    print("Dostępne działania:")
    print("1. Dodawanie (+)")
    print("2. Odejmowanie (-)")
    print("3. Mnożenie (*)")
    print("4. Dzielenie (/)")
    print()

    try:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))

        print("\nWybierz działanie:")
        print("1 - Dodawanie")
        print("2 - Odejmowanie")
        print("3 - Mnożenie")
        print("4 - Dzielenie")

        wybor = input("Twój wybór (1-4): ")

        if wybor == "1":
            print(f"\nWynik: {a} + {b} = {dodaj(a, b)}")
        elif wybor == "2":
            print(f"\nWynik: {a} - {b} = {odejmij(a, b)}")
        elif wybor == "3":
            print(f"\nWynik: {a} * {b} = {pomnoz(a, b)}")
        elif wybor == "4":
            print(f"\nWynik: {a} / {b} = {podziel(a, b)}")
        else:
            print("Nieprawidłowy wybór!")
    except ValueError:
        print("Błąd: Wprowadź poprawne liczby!")

if __name__ == "__main__":
    main()

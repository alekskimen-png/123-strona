@echo off
echo ===== Budowanie strony o kawie =====
echo.

if not exist index.html (
    echo [BLAD] Brak pliku index.html!
    exit /b 1
)
if not exist style.css (
    echo [BLAD] Brak pliku style.css!
    exit /b 1
)
if not exist rodzaje.html (
    echo [BLAD] Brak pliku rodzaje.html!
    exit /b 1
)
if not exist przepisy.html (
    echo [BLAD] Brak pliku przepisy.html!
    exit /b 1
)
if not exist ciekawostki.html (
    echo [BLAD] Brak pliku ciekawostki.html!
    exit /b 1
)

echo [OK] Wszystkie pliki sa na swoim miejscu.
echo.
echo Otwieram strone w domyslnej przegladarce...
start index.html
echo.
echo ===== Budowanie zakonczone! =====
pause

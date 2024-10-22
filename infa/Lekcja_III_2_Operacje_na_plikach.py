# W Pythonie są dwa typy plików: tekstowe i binarne.
# Będziemy zajmowąć się tylko plikami tekstowymi.
# Zawartość pliku tekstowego może być podzielona na wiersze. Każdy wiersz, ewentualnie oprócz ostatniego, kończy się znakiem końca wiersza (zwykle "\n", newline).

# W Pythonie głównym interfejsem do plików zewnętrznych znajdujących się na komputerze jest obiekt plików (file object).

# Obiekt pliku tworzymy za pomocą funkcji open().
# Po użyciu pliku powinno się go zamknąć za pomocą wbudowanej metody close(), aby zwolnić zasoby systemowe powiązane z otwartym plikiem.
# Otwarte pliki są automatycznie zamykane na zakończenie przetwarzania skryptu.

"""
metody (file object):
open(file, mode, encoding) - otwiera plik do odczytu.
    file - nazwa pliku;
    mode - tryb:
        "r" (czytanie, domyślny),
        "w" (pisanie; kasowanie poprzedniej zawartości; utworzy plik, gdy nie istniał),
        "a" (dopisywanie; poprzednia zawartość pozostaje), 
        "x" (tworzenie i otwarcie do zapisu. Błąd, jeżeli plik już istniał),
        "r+" (czytanie i pisanie; poprzednia zawartość pozostaje),
        "w+" (czytanie i pisanie; kasowanie poprzedniej zawartości),
        "a+" (czytanie i pisanie; poprzednia zawartość pozostaje),
        "t" (dodatek do poprzednich, tryb tekstowy, domyślny),
        "b" (dodatek do poprzednich, tryb binarny),
    encoding - kodowanie, dla polskich znaków = "utf-8"
close() - zamyka plik.
readable() - sprawdza czy jest możliwy odczyt z pliku. True (tak)
writable() - sprawdza czy jest możliwy zapis do pliku. True (tak). UWAGA na pisownię metody.
read() - odczyt całej zawartości pliku do str
readline() - odczyt pojedynczej linii do str razem ze znakiem '\n'
readlines() - odczyt całej zawartości pliku i zapis do list[str]. Elementami listy są poszczególne wiersze pliku razem ze znakiem '\n'
write() - zapis str do pliku, zwraca ilość zapisanych znaków.
writelines() - zapis list[str] do pliku, nic nie zwraca
flush() - wymuszenie zapisu do pliku i wyczyszczenie bufora
tell() - podaj pozycję w pliku
seek(offset[, from_what]) - ustawia nową pozycję w pliku i zwraca pozycję po zmianie.
Offset: ilość pozycji  
from_what: określa punkt odniesienia.
Zwraca nową bezwzględną pozycję.
    offset - ku końcowi (dodatni) lub początkowi (ujemny, tylko dla trybu binarnego)
    from_what=0 (domyślnie), od początku pliku
    from_what=1, od bieżącego położenia w pliku
    from_what=2, od końca pliku
"""

# Ustalenie ścieżki

import os
print(os.getcwd())

# Utworzenie obiektu file / otworzenie pliku

# my_path = "C:\\Users\\3c-2\\Python\\"

my_path = ""

my_file_name = "test.txt"

my_file_path = my_path + my_file_name

print(my_file_path)

my_file = open(my_file_path, "w", encoding="utf-8")

# Sprawdzenie możliwości odczytu/zapisu

print(f'Czy jest mozliwość odczytu z pliku? {my_file.readable()}')
print(f'Czy jest mozliwość zapisu do pliku? {my_file.writable()}')


# Zapis do pliku:
# I metoda: write() - zapis str do pliku, zwraca ilość zapisanych znaków.

print(f'Pozycja: {my_file.tell()}')
name = "Bartosz\nKrzysiek\nPawel\nDaniel\n"
baytes_written = my_file.write(name)
print(f'Ilość zapisanych bajtów: {baytes_written}')
print(f'Pozycja: {my_file.tell()}')

# Zamknięcie pliku

my_file.close()

my_file = open(my_file_path, "a", encoding="utf-8")


# II metoda: writelines() - zapis list[str] do pliku, nic nie zwraca
# UWAGA!!! otwieramy plik w trybie "a", aby dopisać nową zawartość.
# Otworzenie pliku w trybie "w" spowoduje usunięcie poprzedniej zawartości

names = ["Mateusz","Dawid","Kacper","Hania"]
# names = ["Mateusz\n","Dawid\n","Kacper\n","Hania\n"]

# for name in names:
#     name = name +"\n"

for i in range(len(names)):
    names[i] = names[i] + "\n"

print(names)

my_file.writelines(names)

names = ["Oliver","Dominik","Kacper","Julia","Karol","Jacek"]

for name in names:
    my_file.write(name + "\n")


# Zamknięcie pliku

my_file.close()




# Odczyt z pliku: 
# I metoda: read() - odczyt całej zawartości pliku do str

print(f'\nI metoda: read() - odczyt całej zawartości pliku do str\n'.center(150, "-"))

my_file = open(my_file_path, "r", encoding="utf-8")
big_str = my_file.read()
print(big_str)

# Zamknięcie pliku

my_file.close()


# II metoda:
# wersja z readline() - odczyt pojedynczej linii do str

print(f'\nII metoda: wersja z readline() - odczyt pojedynczej linii do str\n'.center(150, "-"))

my_file = open(my_file_path, "r", encoding="utf-8")
while True:
    line = my_file.readline()
    if not line:
        break
    print(line, end="")
my_file.close()

# wersja z for

print(f'\nII metoda: wersja z for - odczyt pojedynczej linii do str\n'.center(150, "-"))

my_file = open(my_file_path, "r", encoding="utf-8")
for line in my_file:
    # print(line, end="")
    line = line.rstrip("\n")
    print(line)

my_file.close()

# III metoda: readlines() - odczyt całej zawartości pliku i zapis do list[str]. Elementami listy są poszczególne wiersze pliku

print(f'\nIII metoda: readlines() - odczyt całej zawartości pliku i zapis do list[str]\n'.center(150, "-"))

my_file = open(my_file_path, "r", encoding="utf-8")

lines = my_file.readline()

for line in lines:
    print(line.rstrip("\n"))

my_file.close()

for line in lines:
    my_file = lines.strip()

print(lines)

for i in range(len(lines)):
    lines[i] = lines[i].rstrip("\n")

print(lines)
my_file.close

# WITH - automatyczne zamykanie pliku
print(f'\nIII metoda WITH - automatyczne zamykanie pliku\n'.center(150, "-"))

with open(my_file_path, "r", encoding="utf-8") as my_file:
    for line in my_file:
        print(line.rstrip("\n"))



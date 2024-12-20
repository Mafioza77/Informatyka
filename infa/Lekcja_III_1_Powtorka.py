# -------------------------------------- ------------
# 
# pobranie danych od użytkownika
# input(arg)
# arg - komunikat dla użytkownika
# input() zwraca str (łańcuch znaków)
# 
# --------------------------------------------------

# Zadanie 1. Wczytaj swoje imię, a następnie wypisz je
# dużymi literami oraz podaj jego długość
#  -------------------------------------

# name  = input("Podaj swoje imie: ")
# print(f'Witaj {name.upper()}, Twoje imie ma długość: {len(name)}')

#  -------------------------------------

# --------------------------------------------------
# 
# Instrukcja warunkowa - złożona
# if <warunek>:
#    <lista instrukcji1>
# elif <warunek2>:
#    <lista instrukcji2>
# else:
#    <lista instrukcji3>
# 
# --------------------------------------------------

# Zadanie 2. Napisz program do konwersji temperatury ze °C na °F lub ze °F na °C.
# Wczytaj od użytkownika jednostkę (C/F), a następnie ilość stopni
# i dokonaj przeliczenia na jednostkę docelową.
# Potrzebne wzory:
# °F = (°C * 9/5) + 32
# °C = (°F - 32) * 5 / 9
# Znak stopnia w Windows : Alt + 0176

#  -------------------------------------
# jednostka = input("Czy temperatura jest w °C czy w °F (C/F)")
# temp = float(input("Ile stopni? "))
# if jednostka == "C" or jednostka == "c":
#     print(f'{temp}°C to jest {(temp * 9/5) + 32}°F ')
# elif jednostka in "fF":
#     print(f'{temp}°F to jest {round((temp - 32) * 5 / 9, 2)}°C ')
# else:
#     print(f'{jednostka} jest niepoprawna')
#  -------------------------------------


# --------------------------------------------------
# 
# ternary operator
# Syntax: [on_true] if [expression] else [on_false]
# 
# --------------------------------------------------

# Zadanie 3. Wczytaj temperaturę w °C.
# Jeżeli temp. >  30 lub < 14, to lekcje są odwołane
# Wykorzystaj operator potrójny (ternary) przy wyświetlaniu komunikatu

#  -------------------------------------
# temp = float(input("Podaj ile jest stopni w sali: "))
# komunikat = "odowłane" if temp > 30 or temp < 14 else "trwają :("
# print("Lekcje "+ komunikat)

# print("lekcje odwołane")
#  -------------------------------------


# --------------------------------------------------
# 
# Zakresy (ang. ranges) - niezmienialny, arytmetyczny ciąg liczb.
# 
# Obiekty tego typu tworzymy przy użyciu konstruktora range().
# Przyjmuje on trzy argumenty: start, stop oraz step. W wyniku jest zwracany obiekt reprezentujący
# arytmetyczny ciąg liczb int od start (włącznie, domyślnie 0) do stop (wyłącznie) i różnicach równych step (domyślnie l).
# range(start:0, stop, skok:1)
# 
# --------------------------------------------------

# Zadanie 4. Utwórz zakres od 1 do 15 z krokiem co 3
# i wypisz go jako listę

#  -------------------------------------
# zakres = range(1,15,3)
# print(list(zakres))
#  -------------------------------------

# --------------------------------------------------
# 
# Pętla for
#
# for <iterator> in <sekwencja>
#     <lista_instrukcji1>
# else:
#     <lista_instrukcji2>
#
# --------------------------------------------------


# Zadanie 5. Przypisz do zmiennej surname swoje nazwisko
# Wypisz każdą jego literę za pomocą pętli for iterując po
# - indeksach (od początku do końca i od końca do początku)
# - elementach (znakach)

#  -------------------------------------
# surname = "Piecha"

# for i in range(0, len(surname), 1):
#     print(f'{surname[i]}', end="" if i < len(surname) - 1 else "\n")

# for i in range(len(surname)-1 , -1, -1):
#     print(f'{surname[i]}', end="" if i > 0 else "\n")    

# print(list(range(0, len(surname), 1)))
# print(list(range(len(surname)-1 , -1, -1)))
# #  -------------------------------------

# for char in surname:
#     print(f'{char}', end="")
# else:
#     print()

# print("Coś")

# --------------------------------------------------
# 
# WYCINANIE
# Tworzenie podciągów. Aby utworzyć podciąg bądź wycinek (ang. slice) danego ciągu,
# w nawiasach kwadratowych powinniśmy umieścić obiekt postaci „i : j : k”, gdzie:
# — i (start) jest indeksem pierwszego elementu tworzonego podciągu, domyślna wartość 0;
# — j (stop) jest indeksem końcowym, a ściślej indeksem pierwszego już nas nieinteresującego elementu;
# k <> 0 (step) jest różnicą między kolejnymi elementami tak tworzonego ciągu indeksów, domyślna  wartość 1.
# Domyślne wartości można pominąć.

# S[i:j:k] możemy zastąpić zapisem S[slice(i, j, k)]

# Uwaga: jeżeli pomijamy i, j, lub k w nawiasach kwadratowych, to
# jako argument dla metody slice podajemy "None"

# S[-3::] możemy zastąpić przez S[slice(-3, None, None)] - dostaniemy trzy ostatnie znaki

# Jak widać, funkcji slice() używa się bardzo podobnie do range(). 
#
# --------------------------------------------------


# Zadanie 6. Do rozszyfrowania pliku z wypłatą
# pracownicy CKZiU wykorzystują hasło zbudowane
# z czterech ostatnich cyfr numeru PESEL oraz
# trzech pierwszych liter nazwiska (pierwsza
# litera duża, a dwie kolejne małe)
# Stwórz i wypisz hasło na podstawie poniższych danych

#  -------------------------------------
# pesel = "74102455446"
# surname = "KOWALSKI"

# password = pesel[-4::] + surname[:3:].capitalize()


# print(f'hasło: {password}')
#  -------------------------------------

# --------------------------------------------------
# 
# Listy (ang. lists) - zmienialne, uporządkowane, mogą być duplikaty. Tworzymy przy użyciu nawiasów kwadratowych i przecinków
# 
# Krotki (ang. tuples) - niezmienialne, uporządkowane, mogą być duplikaty. Tworzymy korzystając z nawiasów okrągłych i przecinków.
#
# Zbiory (zestawy) (ang. sets) - niezmienialne, nieuporządkowane, bez duplikatów. Tworzymy korzystając z nawiasów klamrowych i przecinków.
#
# Słowniki (ang. dictionaries) - zmienialne, uporządkowane, bez duplikatów. Tworzymy korzystając z nawiasów klamrowych i przecinków.
# elementy przechowujemy w postaci klucz:wartość
#
# --------------------------------------------------

# Zadanie 7. Na podstawie poniższych imion stwórz listę o nazwie names.
# Następnie:
# - dodaj na koniec listy names swoje imię
# - stwórz z listy zbiór names_set
# - stwórz ze zbioru nową listę names_sorted
# - posortuj listę names_sorted
# - wypisz names_sorted wykorzystując pętle for i iterowanie po elementach


# "Zygfryd", "Alojz", "Gustaw", "Georg", "Markus", "Hans", "Alojz", "Helga", "Hermenegilda", "Alojz"
#  -------------------------------------
names = ["Zygfryd", "Alojz", "Gustaw", "Georg", "Markus", "Hans", "Alojz", "Helga", "Hermenegilda", "Alojz"]

names = list(["Zygfryd", "Alojz", "Gustaw", "Georg", "Markus", "Hans", "Alojz", "Helga", "Hermenegilda", "Alojz"])

names.append("Bartholomäus")

names_set = set(names)

print(names_set)

names_sorted = list(names_set)
names_sorted.sort()

for name in names_sorted:
    print(f'{name}', end = ", ")

#  -------------------------------------
  

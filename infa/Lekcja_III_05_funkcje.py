# WPROWADZENIE
# Funkcja to wielokrotnie używany podprogram (blok kodu).
# Funkcje służą do maksymalizowania możliwości ponownego wykorzystania kodu i minimalizowania powtarzalności kodu
# oraz możliwości powstania błędu.

# DEFINICJA FUNKCJI

"""
def nazwa_funkcji(parametry_funkcji):   # wiersz nagłówkowy
                                        # początek ciała funkcji
    docstring                           # opcjonalnie, opis funkcji
    instrukcje                          # ciało funkcji
    return obiekt_wynikowy              # opcjonalne, zwracana wartość
                                        # koniec ciała funkcji
"""


# NAGŁÓWEK

# Instrukcja def jest kodem wykonywalnym. Tworzy ona obiekt funkcji i przypisuje go do jej nazwy.
# Nazwa funkcji jest najczęściej czasownikiem i powinna być zapisana w notacja snake_case (joined_lower).
# Parametrami funkcji są nazwy zmiennych, które są używane w definicji funkcji do określenia,
# jakie dane są przekazywane do funkcji. Funkcja może być bezparametrowa lub mieć jeden lub kilka
# parametrów — w takim przypadku oddzielamy je przecinkami.

# CIAŁO FUNKCJI:

# Instrukcje w ciele funkcji muszą być poprzedzone odpowiednim wcięciem, gdyż ono właśnie określa,
# co jest częścią ciała, a co już nie.

# I. Docstring - opcjonalny opis funkcji.

# Zalecane formy docstring.
# Postać jednowierszowa.
"""Jeden wiersz zakończony kropką."""

# Postać wielowierszowa.
"""Pierwszy wiersz podsumowania.

Od trzeciego wiersza może być dłuższy opis.
"""

# II. Instrukcje - W ciele funkcji możemy użyć wszystkiego, czego nauczyliśmy się do tej pory — zmienne,
# pętle, instrukcje warunkowe czy nawet same funkcje.


#. III. Zwracanie wartości przez funkcję. Jeżeli nie użyjemy słowa kluczowego return lub
#  podamy tylko samo słowo return, to funkcja zwróci wartość None. Przez podanie nazwy zmiennej po słowie return
#  możemy zwrócić pojedynczą wartość (int, float, bool, obiekt itd.) lub kolekcję (np. listę, zbiór, krotki)

# W poniższej definicji funkcji parametrem jest zmienna lokalna o nazwie 'name'. Funkcja zwraca None.
def hello_name(name):
    """Wita użytkownika, o nazwie name."""
    print(f'Hello, {name}')
    return name

# WYWOŁANIE FUNKCJI

# Aby wywołać funkcję, używamy jej nazwy oraz nawiasów okrągłych, w których podajemy argumenty funkcji.
# Argumenty, to wartości, które przekazywane są do funkcji i przypisywane odpowiadającym im parametrom (zmiennym funkcji).
# Ilość i kolejność argumentów (wartości w nawiasie przy wywołaniu) powinna odpowiadać ilości i kolejności parametrów
# (zmiennych w nawiasie w definicji) - można to obejść stosując domyślne parametry i nazwane argumenty.

# Następnie wykonywane są kolejno instrukcje jej ciała. Na końcu zwracana jest wartość funkcji (None lub jakaś określona )

hello_name("Jack")

# POLIMORFIZM (WIELOPOSTACIOWOŚĆ)
# W Pythonie nie ma deklaracji typu parametrów, dlatego cechą funkcji jest polimorfizm:
# Zachowanie funkcji zależy od tego, co do niej przekażemy.

def times(x, y):
    """Zwraca iloczyn parametrów."""
    return x * y   

print(times(2, 3))                   # 6
print(times(2, 3.14))                # 6.28
print(times("Bum!", 3))              # "Bum!Bum!Bum!"

# Polimorficzna funkcja len().

print(len("Python"))                      # 6, długość stringu = liczba znaków
print(len(["Python", "C++", "Java"]))     # 3, liczba elementów listy
print(len({"Name": "Adam", "Age": 30}))   # 2, liczba elementów słownika
print(len(set([1, 3, 5, 7])))             # 4, liczba elementów zbioru


# Zadanie 1. Dokonaj uproszczenia poniższego skryptu
# (wypisującego dziwną wersję piosenki urodzinowej)
# zastępując powtarzające się fragmenty kodu
# bezparametrową funkcją o nazwie happy_birthday()

#  -------------------------------------
print("Happy birthday to you!")
print("Your are old my friend!")
print("Happy birthday, happy birthday!")
print()

print("Happy birthday to you!")
print("Your are old my friend!")
print("Happy birthday, happy birthday!")
print()

print("Happy birthday to you!")
print("Your are old my friend!")
print("Happy birthday, happy birthday!")
print()

#  -------------------------------------
def times(x, y):
    """Happy birthday to you!\nYour are old my friend!\nHappy birthday, happy birthday\n"""
    return x * y  

print(times("Happy birthday to you!\nYour are old my friend!\nHappy birthday, happy birthday\n", 3))
#  -------------------------------------


# Zadanie 2. Dodaj nową funkcją happy_birthday_v2(name), która
# jest modyfikacją happy_birthday().
# Parametr name, to imię solenizanta. W ciele funkcji
# przypisana do niego wartość ma zastąpić "you" w pierwszej linijce tekstu)
# Wywołaj funkcję dla trzech solenizantów: Johna, Oliviera, Paula.
"""
def nazwa_funkcji(parametry_funkcji):   # wiersz nagłówkowy
                                        # początek ciała funkcji
    docstring                           # opcjonalnie, opis funkcji
    instrukcje                          # ciało funkcji
    return obiekt_wynikowy              # opcjonalne, zwracana wartość
                                        # koniec ciała funkcji
"""
#  -------------------------------------
def happy_birthday_v2(name):
    """Druga wersja funkcji happy_birthday"""

    print(f'Happy birthday to {name}!')
    print("Your are old my friend!")
    print("Happy birthday, happy birthday!")
    print()
       
    return name
happy_birthday_v2("John")
happy_birthday_v2("Oliver")
happy_birthday_v2("Paul")

#  -------------------------------------

# Zadanie 3. Dodaj nową funkcją happy_birthday_v3(name, age), która
# jest modyfikacją happy_birthday_v2().
# Parametr name, to imię solenizanta, a parametr age, to oczywiście jego wiek.
# W ciele funkcji zmienna age ma być wstawiona między "are" i "old"
# w drugiej linijce tekstu) - dodaj też "years " przed old.
# Wywołaj funkcję dla trzech solenizantów: Johna (18 lat), Oliviera (16 lat), Paula (20 lat).



#  -------------------------------------
def happy_birthday_v3(name, age):
    """Trzecia Wersja Funkcji happy_birthday
    
    name - imie solenizanta,

    age - jego wiek
    
    """
    print(f'Happy birthday to {name}!')
    print(f'Your are {age} years  old my friend!')
    print("Happy birthday, happy birthday!")
    print()

happy_birthday_v3("John", 18)
happy_birthday_v3("Oliviera", 16)
happy_birthday_v3("Paula", 20)
#  -------------------------------------

# Zadanie 4. Wywołaj funkcję happy_birthday_v3(name, age), zamieniając argumenty miejscami.
# Czy można tak robić? Czy kolejność argumentów ma znaczenie?

#  -------------------------------------
def happy_birthday_v3(name, age):

    """Trzeba przestrzegac kolejnosci argumentow poniewaz wyjda GŁUPOTY"""

    print(f'Happy birthday to {name}!')
    print(f'Your are {age} years  old my friend!')
    print("Happy birthday, happy birthday!")
    print()

happy_birthday_v3(18, "John")
happy_birthday_v3("Oliviera", 16)
happy_birthday_v3("Paula", 20)
print("----------------------------------------------------------------")

#  -------------------------------------

# Zadanie 5. Wywołaj ponownie funkcję happy_birthday_v3(name, age), zamieniając argumenty miejscami.
# Tym razem nazwij argumenty, tzn. przed przekazywanymi wartościami wpisz nazwy parametrów:
# age=18, name="John"
# Jak tym razem zachował się Python?

#  -------------------------------------
def happy_birthday_v3(age=16, name="John"):

    print(f'Happy birthday to {name}!')
    print(f'Your are {age} years  old my friend!')
    print("Happy birthday, happy birthday!")
    print()

happy_birthday_v3(18, "John")
happy_birthday_v3("Oliviera", 16)
happy_birthday_v3("Paula", 20)


#  -------------------------------------

# Zadanie 6. Dodaj nową funkcją happy_birthday_v4(name, age), która
# jest modyfikacją happy_birthday_v3(). Modyfikacja ma polegać na dodaniu w definicji funkcji
# wartości domyślnych dla parametrów name i age. Dla name ma to być "you", a dla age 18.
# Sprawdź co się stanie, jeżeli wywołamy funkcję happy_birthday_v4:
# - jedynie z wartością dla argumentu name;
# - jedynie z wartością dla nazwanego argumentu age;
# - nie podając żadnego argumentu.
# A co się stanie, jeżeli pominiemy którykolwiek z argumentów funkcji happy_birthday_v3()?

#  -------------------------------------
print("----------------------------------------------------------------")
def happy_birthday_v4(age=18, name="you"):

    print(f'Happy birthday to {name}!')
    print(f'Your are {age} years  old my friend!')
    print("Happy birthday, happy birthday!")
    print()


happy_birthday_v4(name="Bartosz")
happy_birthday_v4(age= 122)
happy_birthday_v4()

#  -------------------------------------


# Zadanie 7. Zwracanie wartości przez funkcję.
# Napisać cztery funkcje (add, subtract, multiply, divide) wykonujące operacje dodawania, odejmowania, mnożenia i dzielenia.
# Parametrami funkcji są dwie liczby, a zwracaną wartością wynik konkretnej operacji arytmetycznej.  
#  -------------------------------------
def add(a, b):
    """Dodawanie"""
    return a + b
def subtract(a, b):
    """Odejmowanie"""
    return a-b
def multiply(a, b):
    """Mnożenie"""
    return a*b
def divide(a, b):
    """Dzielenie"""
    if b!=0:
        return a/b
    else:
        print("ERROR")

print(add(6,3))
print(subtract(6,3))
print(multiply(6,3))
print(divide(6,3))

#  -------------------------------------


# Zadanie 8. Zwracanie wartości przez funkcję.
# Napisać funkcję create_name(name, surname), która zwróci połączone wartości w name i surname oddzielone spacją.
# Wszystkie litery (oprócz pierwszych) mają być małe.
#  -------------------------------------
def create_name(name, surname):
    return name.capitalize() + " " + surname.capitalize()
#  -------------------------------------
def create_name_v2(name, surname):
    return (name + " " + surname).title()
#  -------------------------------------
def create_name_v3(name, surname):
    return " ".join([name, surname]).title()
#  -------------------------------------
print(create_name("BARTOSZ", "PIECHA"))
print(create_name_v2("BARTOSZ", "PIECHA"))
print(create_name_v3("BARTOSZ", "PIECHA"))
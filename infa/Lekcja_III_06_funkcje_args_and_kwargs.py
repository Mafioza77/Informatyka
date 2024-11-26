# Dotychczas poznaliśmy sposoby wywoływania funkcji z:

# 1. argumentami pozycyjnymi (positional arguments)
# , gdzie ilość i kolejność argumentów (wartości w nawiasie przy wywołaniu) powinna odpowiadać ilości i kolejności parametrów
# (zmiennych w nawiasie w definicji)

#  -------------------------------------
def happy_birthday_v3(name, age):
    print(f"Happy birthday to {name}!")
    print(f"Your are {age} years old my friend!")

happy_birthday_v3("John", 18)
#  -------------------------------------


# 2. brakującymi argumentami dla parametrów, którym przypisaliśmy wartości domyślne (default) w definicji funkcji.

#  -------------------------------------
def happy_birthday_v3(name, age=18):
    print(f"Happy birthday to {name}!")
    print(f"Your are {age} years old my friend!")

happy_birthday_v3("John")
#  -------------------------------------

# 3. argumentami nazwanymi (keyword) - dzięki czemu argumenty wywoływanej funkcji nie musiały mieć takiej samej
#  kolejności jak parametry

#  -------------------------------------
def happy_birthday_v3(name, age):
    print(f"Happy birthday to {name}!")
    print(f"Your are {age} years old my friend!")

happy_birthday_v3(age=15, name="John")
#  -------------------------------------


# 4. dowolna ilość argumentów (arbitrary arguments)

# Przekazywanie dowolnej ilości argumentów do funkcji możemy zrealizować przez:
# *args     = argumenty nie są nazwane, nie posiadają kluczy (non-key arguments)
# **kwargs  = argumenty są nazwane, mają klucz (keyword-arguments)
#           * operator rozpakowujący (unpacking operator)

# Mamy funkcję obliczającą sumę:

#  -------------------------------------
def add(number_x, number_y):
    result = number_x + number_y
    return result

print(add(3, 5))
#  -------------------------------------

# Zadanie 1: Napisz nową wersję funkcji add_new(*args), która obliczy i zwróci sumę
# dla dowolnej ilości liczb przekazywanych jako argumenty przy wywołaniu funkcji.
# Należy w ciele funkcji sprawdzić jaki typ jest wykorzystywany
# do przekazywania sekwencji argumentów.

#  -------------------------------------
def add_new(*args):
    result = 0
    #print(type(args))
    for arg in args:
        result = result + arg
        #result += arg
    return result
#  -------------------------------------

print(add_new(5, 7))
print(add_new(5, 7,312,412))

# A gdyby była lista numerów do przekazania?
number_list = [145, -7, 2, 6, 45]
#  -------------------------------------
print(add_new(*number_list))
#  -------------------------------------


# Zadanie 2: Napisz nową wersję create_name_new(*args) zwracającą pełną nazwę osoby na podstawie
# dowolnej ilości tytułów, imion, nazwisk przekazywanych jako argumenty przy wywołaniu funkcji.
# Należy zachować sposób wyświetlania/łączenia łańcuchów, tzn. pierwsza litera duża, a kolejne małe.

#  -------------------------------------
def create_name_new(*args):
    result = ""
    for arg in args:
    #     result += arg.capitalize() + ","
    # return result
        result += arg + " "
    return result.title().rstrip(" ")
    

print(create_name_new("bartosz", "piecha","dawidek"))

#  -------------------------------------
#  wersja z join
def create_name_new_v2(*args):
    return " ".join(args).title()


print(create_name_new_v2("bartosz", "piecha","dawidek"))
#  -------------------------------------

# Zadanie 3: Napisz funkcję print_address(**kwargs) wypisujący adres
# na podstawie dowolnej ilości nazwanych argumentów.
# Sprawdź w ciele funkcji jaki typ sekwenycjny wykorzystywany jest do
# przekazywania argumentów.


#  -------------------------------------
def print_address(**kwargs):
    #print(type(kwargs))
    # for key, valeu in kwargs.items():
    #     print(f'{key} : {valeu}')
    return f'{kwargs['rodzaj']} {kwargs['ulica']} {kwargs['nr_domu']}{"/" + kwargs['nr_lokalu'] if kwargs.get('nr_lokalu') else ""} {kwargs['kod']} {kwargs['miasto']}'

print(print_address(rodzaj="ulica", ulica="Nowa", nr_domu="3c", nr_lokalu="3", kod="47-400", miasto="Racibórz"))
print(print_address(rodzaj="ulica", ulica="Nowa", nr_domu="3c", kod="44-100", miasto="Gliwice"))

#  -------------------------------------



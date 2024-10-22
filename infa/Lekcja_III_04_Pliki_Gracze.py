"""
W pliku gracze.txt przechowywane są dane o miłośnikach gier planszowych.
Twoim zadaniem jest:
1. Ustalenie znaku separatora;
2. Policzenie średniej wieku graczy i zapisanie wyniku (dokładność: jedno miejsce po przecinku) do pliku gracze_wynik.txt;
3. Policzenie częstości występowania imion graczy i zapisanie wyników w posortowanej kolejności do pliku gracze_wynik.txt.
    
Przykładowa zawartość pliku gracze_wynik.txt:
    
Średnia wieku graczy wynosi: 54.1 lat

     Imię      : Ilość wystąpień 
Adam           :                5
Adela          :                1
Adrian         :                4
Adriana        :                1
Adrianna       :                2
Agata          :                3
Agnieszka      :                1
Aisha          :                2

 
"""

average_age = 0

ages_list = []
names_list = []

gamers_input = open("gracze.txt" , "r", encoding="utf-8")
line = gamers_input.readline()
for line in gamers_input:
    temp_line = line.rstrip("\n")
    temp_list = temp_line.split("\t")
    ages_list.append(int(temp_list[-1]))
    names_list.append(temp_list[1])

gamers_input.close()

average_age = sum(ages_list) / len(ages_list)

gamers_output = open("gracze_wynik.txt", "w", encoding="utf-8")
gamers_output.write(f'Średnia wieku graczy wynosi: {average_age:.1f} lat\n\n')
gamers_output.write(f'{"Imię":^15}:{"Ilość wystąpień":^17}\n')

# ^ = center
# < = left
# > = right

name_set = set(names_list)

name_list_sorted = list(name_set)
name_list_sorted.sort()
for name in name_list_sorted:
    gamers_output.write(f'{name:<15}:{names_list.count(name):>17}\n')

print(name_list_sorted)
print(name_set)

gamers_output.close()
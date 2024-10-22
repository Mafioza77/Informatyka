"""
Zadanie: W pliku tm_students.txt przechowywane są dane o uczniach TM. Policz ilość uczniów w każdej klasie.

Struktura pliku: (nagłówek + dane)

Klasa;Imię;Nazwisko
1aT;Szymon;Augustyniak
1aT;Tobias;Bielan


Z pliku tm_students.txt należy odczytać dowolną metodą dane i pozyskać z nich nazwy klas (wiersz z nagłówkiem należy zignorować).
Wykorzystując listy, zbiory lub słowniki należy policzyć ilość uczniów w każdej klasie i
zapisać posortowane po nazwie klasy dane do pliku wynikowego tm_classes.txt. 

Przykład zawartości pliku wynikowego tm_classes.txt:

 Klasa : Ilość uczniów
  1aB  :      32      
  1aT  :      32      
  1bB  :      32      
  1bT  :      29         


"""
students_file = open("tm_students.txt", "r",encoding="utf-8")

classes_list = []


students_file.readline()
for line in students_file:
    temp_line = line.rstrip("\n")
    temp_list = temp_line.split(";")
    classes_list.append(temp_list[0])
    
classes_set = set(classes_list)

classes_list_sorted = list(classes_set)
classes_list_sorted.sort()

print(classes_set)
print(classes_list_sorted)


students_file.close()

classes_file = open("tm_classes.txt", "w", encoding="utf-8")

classes_file.write("Klasa".center(7) + ":" + "Ilość uczniów".center(16) + "\n")
for clas in classes_list_sorted:
    classes_file.write(clas.center(7)+ ":" + str(classes_list.count(clas)).center(14)+ "\n")
classes_file.close()

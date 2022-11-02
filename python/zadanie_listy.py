
country = ['Poland', 'Japan', 'Korea', 'Sweden', 'Denmark']

x = input('Podaj nowy kraj: ')
y = input('Podaj kolejny kraj: ')

country.append(x)
country.append(y)

print("-----------MENU")
print("1) Wyświetl pierwsze 3 elementy listy")
print("2) Wyświetl elementy listy, które dodałem (dane pobierz z listy)")
print("3) Wyświetl zawartość listy")
print("4) Wyczyść zawartość listy")
print("5) Znajdź element w liście, który poda użytkownik (wyświetl czy jest dodany do listy)")
print("6) KONIEC")

while True:
    wybor = input('Wybierz opcję (1-5): ')

    if wybor == '1':
        threeElememts = country[0:3]
        print('Pierwsze trzy elementy listy: ', threeElememts)
    elif wybor == '2':
        addedElements = country[-2:]
        print('Dodane kraje: ', addedElements)
    elif wybor == '3':
        print(country)
    elif wybor == '4':
        country.clear()
        print('Wyczyszczono listę!')
    elif wybor == "5":
        wzorzec = input('Podaj kraj który chcesz sprawdzić: ')
        if wzorzec in country:
            print('Tak, ten kraj znajduje się na liście')
        else:
            print('Nie, ten kraj nie znajduje się na liście')
    elif wybor == '6':
        break

print("--------------------------")
print("Zawartość listy po wykonaniu operacji przez uzytkownika: ", country)

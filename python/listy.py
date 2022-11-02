programowanie = ['Python', 'PHP', 'C#']
print(programowanie)
print(type(programowanie))
first = programowanie[0]
print("Pierwszy element: ", first)

threeElememts = programowanie[0:3]
# print

lastelement = programowanie[-1]
print("Last element: ", lastelement)

# dodanie nowego elementu na koniec listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

# zliczanie elementu w liście
countElements = programowanie.count('Python')
print(countElements)

# zliczanie wszytskich elementów w liście
countElementsOfList = len(programowanie)
print('Ilość elementów w liście: ', countElementsOfList)
print("Ilość elementów w liście " + str(countElementsOfList))

# połączenie list
anotherList = ['C', 'C++']
programowanie.extend(anotherList)

# usuwanie elementów z listy

# nie kopiujejmy  tablicy tylko dajemy odnosnik do orginalnej - obie sie usuna
new = programowanie
new.clear()
print('New list: ' + str(new))

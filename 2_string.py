
text="Jakub, Marek, Zuzia"
print(type(text)) #wyświetlanie typu zmienniej

tab=text.split(', ') #podzial na elementy tablicy
print(tab)
print(type(tab))

name1=tab[0]
print(name1)

nameUpper=name1.upper()
print(nameUpper)
nameLower=name1.lower()
print(nameLower)

#sprawdzenie zawartości true-zawiera dane (tylko litery), false-nie zawiera
surname=input()
content=surname.isalpha()
print(content)

#biale znaki
print("Jan \nKowalski")
text1="Anna\n"
text2="Nowak"
print(text1 + text2)
text1=text1.rstrip() #funkcja wylącza działanie białych znaków
print(text1 + text2)

print(f'{text1} {text2}')
text="%s, Java i %s" % ("PHP", "Python")
print(text)
text="{1}, Java i {0}".format("PHP", "Python")
print(text)
#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

print('test1', end='')
print('test')
year=2022
month=10
day=12
print(day, month, year, sep='-')
print(day, month, year, sep='/')

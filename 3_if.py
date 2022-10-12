x=input('Podaj wartość: ')

if(x=='10'):
    print('Podałeś 10')
else:
    print('Inna waertość niż 10')

y=False
if y:
    print('prawda')
else:
     print('fałsz')

'''
Użytkownik podaje wartości trzech zmiennych x, y, z.
Wyświetl która z tych trzech wartości jest największa.
Wykorzystaj instrukcje warunkowe
'''

x=input('Podaj x: ')
y=input('Podaj y: ')
z=input('Podaj z: ')

if(x>y)and(x>z):
    print('Największy jest x')

elif(y>x)and(y>z):
    print('Największy jest y')

else:
    print('Największy jest z')

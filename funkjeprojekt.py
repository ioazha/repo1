#zad5
def slownik(slowo):
    lancuch=" "
    if slowo == "jeden":
        return "one"
    elif slowo == "dwa":
        return "two"
    elif slowo == "trzy":
        return "three"
    elif slowo=="cztery":
        return "four"
    elif slowo=="pięć":
        return "five"
    else:
        return lancuch
    
lista = [1,2,3,4,5,6]
print(lista)

#zad4
# def zamiana(lancuch):
#     wynik= lancuch[-1]+lancuch[1:-1]+lancuch[:1]
#     return wynik
#
# print("Podaj łancuch znaków")
# lancuch=input()
# print(zamiana(lancuch))

#zad3
# import random
# def los(liczba):
#     for liczba in alfabet:
#         lancuch = random.choice(alfabet)
#     return lancuch
# alfabet="abcdefghijklmnoprstuwyz"
# print("Wpisz ile literek chcesz wylosować")
# liczba=int(input())
# print(los(liczba))

#zad2
# def usun(nr):
#     if nr==0 or nr==2 or nr==3 or nr==4 or nr==5 or nr==6 or nr==7 or nr==8 or nr==9:
#         return nr
# print("Wpisz nr telefonu")
# nr=input()
# print(usun(nr))

#zad1
# def liczby(lista):
#     for liczba in lista[:]:
#         if lista%2==0:
#             lista.remove(liczba)
# print("Podaj 5 liczb całkowitych")
# lista=input()
# print(liczby(lista))

"""
A csoport
Szimuláljuk egy 20 oldalú D&D kocka 100 db dobását! A dobásokat egy listában tároljuk! Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 6-os a dobások között?
2. Hányadikra sikerült először 18-nál nagyobbat dobni?
3. Hány darab 1-est dobtak?
4. Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt?
5. Mennyi a 4-es dobások szorzata?
"""

dobasok = []

import random

random_szamok = [random.randint(1,20) for _ in range(100)]

dobasok.append(random_szamok)

print(dobasok)

print("1. Feladat")
if 6 in random_szamok:
    print("A dobások között volt 6-os.")
else:
    print("Nem volt a dobások között 6-os.")

print("2. Feladat")
tnyolcnal_nagyobb = [i for i, dobas in enumerate(random_szamok) if dobas > 17]
print(tnyolcnal_nagyobb[0])

print("3. Feladat")
print(random_szamok.count(1))

print("4. Feladat")


print("5. Feladat")
negyesek = random_szamok.count(4)
szorzat = 4 ** negyesek
print(szorzat)
import random
from itertools import repeat

import beolvas
import math

import beolvas

from  random import *


def harom():
    # 1. megoldás
    for i in range(0, 21, 1):
        print(i)

    # 2. megoldás
    for i in range(21):
        print(i)

    #3. megoldás
    for i in range(0, 21):
        print(i)

    #4.megoldás
    i = 0
    while i < 21:
        print(i)
        i += 1


def negy():
    for i in range(20, 57, 2):
        print(i)


def ot():
    for i in range(77, -77, -4):
        print(i)


def beolvas():
    szam = float(input("Kérem adjon meg egy valós számot!"))
    return szam


def hat():
    #6.	Kérj be 2 számot, majd írasd ki a számokat a legkisebbtől a legnagyobbig! (a legnagyobbat is! Ha az első szám nagyobb, abban az esetben is a legkisebbtől a legnagyobbig írasd ki!)

    szam1 = beolvas()
    szam2 = beolvas()

    # melyik a nagyobb
    if szam2 < szam1:
        # csere
        atmenet = szam1
        szam1 = szam2
        szam2 = atmenet

    for i in range(szam1, szam2 + 1, 1):
        print(i, end=" ")


def het():
    #7.	Kérj be 2 számot, majd írasd ki a számokat 0-tól a 2 szám szorzatáig!
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    if szorzat < 0:
        for i in range(0, szorzat - 1, -1):
            print(i, end=" ")
    else:
        for i in range(0, szorzat + 1, 1):
            print(i, end=" ")


def nyolc():
    # 8.	Kérj be 2 számot, majd írasd ki a számokat 0-tól a 2 szám szorzatáig!
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    if szorzat < 0:
        i = 0
        while i < szorzat - 1:
            print(i, end=" ")
            i -= 1  #i = i-1
            #for i in range(0, szorzat - 1, -1):
            print(i, end=" ")
    else:
        i = 0
        while i < szorzat + 1:
            print(i, end=" ")
            i += 1
            #for i in range(0, szorzat + 1, 1):
            print(i, end=" ")


def kilencA():
    #1. megoldás
    for szam in range(0, 7, 1):
        print(str(szam) + ",", end="")
    print(7)
    #2.megoldás
    """
    print(0, end="")
    for szam in range(1,8,1):
        print(","+str(szam),end="")
    """


def tizenegy():
    #11.Írasd ki 2 bekért szám (x és y) alapján, hogy mennyi 3x+y2!
    x = beolvas2()
    y = beolvas2()

    eredmeny = 3 * x + y ** 2
    eredmeny1 = 3 * x + math.pow(y, 2)
    eredmeny2 = 3 * x + pow(y, 2)
    eredmeny3 = 3 * x + (y * y)
    print("3*" + str(x) + "+" + str(y) + "^2=" + str(eredmeny))


def tizenketto():
    #12.	Számold meg 2 bekért szám közötti páros számokat! (pl. hány db páros szám van 4 és 31 között?)
    x = beolvas2()
    y = beolvas2()
    #  print(math.floor(x))
    #  print(math.ceil(y))
    db = 0
    for szam in range(math.ceil(x), round(y) + 1, 1):
        # print(szam, end=" ")
        if szam % 2 == 0:
            #páros
            db += 1
    print("A páros számok száma: " + str(db) + ".")

#ciklus 2 gyakorlás
def tizennegy():
    #Írjuk ki a számokat 1-től 100-ig oly módon,hogy ha egy szám 3-mal osztható, akkor a szám helyett írjuk azt, hogy BIM, ha kettővel osztható, akkor írjuk azt, hogy BAMM, és ha 2-vel is és 3-mal is osztható, akkor írjuk, hogy BIM-BAM, egyéb esetben írjuk ki a számot!
    for szam in range(0, 101):
        #3-al osztható
        if szam % 2 == 0 and szam % 3 == 0:
            print("Bim-Bam")
        elif szam % 3 == 0:
            print("Bim")
        elif szam % 2 == 0:
            print("Bamm")
        else:
            print(szam)


def tizenot():
    #Írjuk ki a prím számokat 100-ig!
    for szam in range(2, 101):
        is_prime = True
        for i in range(2, szam):
            if szam % i == 0:
                is_prime = False
                break
        if is_prime:
            print(szam)
def tizenhat():
    negyzetszamosszeg = 0
    for szam in range(1,11):
        negyzetszamosszeg += szam ** 2
    print("Az első tíz négyzetszám összege", negyzetszamosszeg)

def tizenhet():
    #Írjunk ki 1-10 értékhatár közé eső 10 véletlen számot, majd írjuk ki ezek összegét!
    szam1 = [randint(1,10) for _ in range(10)]
    osszeg = sum(szam1)

    print("Véletlenszámok:",szam1)
    print("Összegük:", osszeg)

def tizennyolc():
    #Írjunk ki 1-10 értékhatár közé eső 10 véletlen számot, s mondjuk meg, hány páros van közöttük!
    szam1 = [randint(1, 10) for _ in range(10)]
    print(szam1)
    db = 0
    for szam1 in range(1,11):
        # print(szam, end=" ")
        if szam1 % 2 == 0:
            # páros
            db += 1
    print("A páros számok száma: " + str(db) + ".")


#ciklus 1
def tizennegy2():
    #Add össze 10 bekért számnál a negatív számokat!
    negativesum = 0
    for _ in range(10):
        szam1 = int(input("Adj meg egy számot:"))
        if szam1 < 0:
            negativesum += szam1
    print("A negatív számok összege:",negativesum)

def tizenot2():
    #Kérj be számot mindaddig, amíg negatív és 3-mal osztható nem lesz!

    szam1 = float(input("Adj meg egy számot:"))
    while szam1 >=0 or szam1%3 !=0:
        print("A szám nem negatív,vagy nem osztható hárommal. Próbáld újra")
        szam1 = float(input("Adj meg egy számot:"))
    print(f"A szám {szam1} negatív és osztható hárommal.")

def tizenhat2():
    #Kérj be számot mindaddig, amíg 3 jegyű pozitív szám nem lesz!
    szam1 = float(input("Adj meg egy számot:"))
    while szam1<0 or szam1<100 or szam1>1000:
        print("A szám nem háromjegyű vagy nem pozitív")
        szam1 = float(input("Adj meg egy számot:"))
    print(f"A szám {szam1} pozitív és háromjegyű")

def tizenhet2():
    #Kérj be 5 számot, és az összegüket írasd ki!
    sum = 0
    for _ in range(5):
        szam1 = int(input("Adj meg egy számot:"))
        sum += szam1
    print("A számok összege:", sum)

def tizennyolc2():
    #Kérj be 5 szöveget, és fűzd őket össze space-szel, majd írasd ki a kész szöveget!

    szoveg1 = str(input("Adja meg az első szövegrészletet:"))
    szoveg2 = str(input("Adja meg a második szövegrészletet:"))
    szoveg3 = str(input("Adja meg a harmadik szövegrészletet:"))
    szoveg4 = str(input("Adja meg a negyedik szövegrészletet:"))
    szoveg5 = str(input("Adja meg az ötödik szövegrészletet:"))
    print(szoveg1," "+szoveg2," "+szoveg3," "+szoveg4," "+szoveg5," ")

def tizenkilenc2():
    #Kérj be 5 számot, és a legkisebbet írasd ki!

    szamok = []
    for i in range(5):
        szam1 = int(input(f"Adj meg a {i+1}. számot:"))
        szamok.append(szam1)

    legkisebb = min(szamok)

    print(f" A legkisebb szám:{legkisebb}")

def husz2():
    #Kérj be 5 számot, és döntsd el, hogy van-e köztük páros!
    for i in range(5):
        szam1 = int(input(f"Adjon meg egy {i + 1}. számot:"))
        if szam1 % 2 ==0:
            paros_van = True
    if paros_van:
            print("Van páros szám.")
    else: print("Nincs páros szám")

def huszonegy2():
    #Kérj be 5 számot, és döntsd el, hogy van-e köztük páros, majd ezt a számot add is meg, ha van ilyen!
    szamok=[]
    for i in range(5):
        szam1 = int(input(f"Adjon meg egy {i + 1}. számot:"))
        szamok.append(szam1)

    paros_szamok = [szam1 for szam1 in szamok if szam1 % 2 ==0]

    if paros_szamok:
        print(f" A megadott számok között van páros szám:Ezek a következők:",paros_szamok)
    else:
        print("Nincs páros szám a megadott számok között.")

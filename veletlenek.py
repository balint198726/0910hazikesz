import random

from beolvas import *
from random import *
def egyAlap():
    szam1 = beolvasEgesz()
    if  szam1%2 == 1:
        print("Páratlan.")
    else:
        print("Páros")

def egyAlapA():
    szam1 = randint(-10,10)
    print(szam1)
    if  szam1%2 == 1:
        print("Páratlan.")
    else:
        print("Páros")


def egyAlapB():
    szam1 = randint(-10, 10)
    #print("szám:"+str(szam1))
    while not(szam1%2==0):
        szam1 = randint(-10,10)
        #print("újszám:"+str(szam1))
    print(szam1**2)

def egyAlapC():
    szam1 = generalParosEgesz()
    print(szam1 ** 2)

def kettoalap():
    szam1 = beolvasEgesz()
    if 1 <= szam1 <= 12:
        #jóesetek
        if szam1==1:
            print("Január")
        elif szam1==2:
            print("Február")
        elif szam1==3:
            print("Március")
        elif szam1==4:
            print("Április")
        elif szam1==5:
            print("Május")
        elif szam1==6:
            print("Június")
        elif szam1==7:
            print("Július")
        elif szam1==8:
            print("Augusztus")
        elif szam1==9:
            print("Szeptember")
        elif szam1==10:
            print("Október")
        elif szam1==11:
            print("November")
        else:
            print("December")

    else:
        print("Hiba: nem megfelelő szám.")
def kettoalapb():
    #szam1 = randint(1,12) csupa jók
    szam1 = randint(-5,15)
    #szam1 = randint(-100,100) sok rossz érték
    print("Hónap sorszáma:"+str(szam1))
    if szam1>=1  and szam1 <=12:
        #jóesetek
        if szam1==1:
            print("Január")
        elif szam1==2:
            print("Február")
        elif szam1==3:
            print("Március")
        elif szam1==4:
            print("Április")
        elif szam1==5:
            print("Május")
        elif szam1==6:
            print("Június")
        elif szam1==7:
            print("Július")
        elif szam1==8:
            print("Augusztus")
        elif szam1==9:
            print("Szeptember")
        elif szam1==10:
            print("Október")
        elif szam1==11:
            print("November")
        else:
            print("December")

    else:
        print("Hiba: nem megfelelő szám.")

def kettoalapc():
    #szam1 = randint(1,12) csupa jók
    szam1 = randint(-5,15)
    #szam1 = randint(-100,100) sok rossz érték
    print("Hónap sorszáma:"+str(szam1))
    if szam1>=1  and szam1 <=12:
        #jóesetek
        if szam1==1:
            print("Január")
        elif szam1==2:
            print("Február")
        elif szam1==3:
            print("Március")
        elif szam1==4:
            print("Április")
        elif szam1==5:
            print("Május")
        elif szam1==6:
            print("Június")
        elif szam1==7:
            print("Július")
        elif szam1==8:
            print("Augusztus")
        elif szam1==9:
            print("Szeptember")
        elif szam1==10:
            print("Október")
        elif szam1==11:
            print("November")
        else:
            print("December")

    else:
        print("Hiba: nem megfelelő szám.")

def haromalap():
    szam1 = beolvasTort()
    if 0 <= szam1 <= 360:
        #jóesetek
        if szam1==0:
            print(str(szam1)+" fok,azaz Nullszög")
        elif 0 < szam1 < 90:
            print(str(szam1)+" fok,azaz Hegyesszög")
        elif szam1==90:
            print(str(szam1)+" fok,azaz Derékszög")
        elif 90 < szam1 < 180:
            print(str(szam1)+" fok,azaz Tompaszög")
        elif szam1 == 180:
            print(str(szam1)+" fok,azaz Egyenesszög")
        elif  180 < szam1 < 360:
            print(str(szam1)+" fok,azaz Homorúszög")
        else:
            print(str(szam1)+" fok,azaz Teljesszög")
    else:
        print("Szám nem megfelelő")

def haromalapa():
    szam1 = uniform(-100,500)
    if 0 <= szam1 <= 360:
        #jóesetek
        if szam1==0:
            print(str(szam1)+" fok,azaz Nullszög")
        elif 0 < szam1 < 90:
            print(str(szam1)+" fok,azaz Hegyesszög")
        elif szam1==90:
            print(str(szam1)+" fok,azaz Derékszög")
        elif 90 < szam1 < 180:
            print(str(szam1)+" fok,azaz Tompaszög")
        elif szam1 == 180:
            print(str(szam1)+" fok,azaz Egyenesszög")
        elif  180 < szam1 < 360:
            print(str(szam1)+" fok,azaz Homorúszög")
        else:
            print(str(szam1)+" fok,azaz Teljesszög")
    else:
        print("Szám nem megfelelő")

def negyedik():
    #Kérj be ellenőrzötten egy negatív számot, majd add meg az abszolút értékét!
    szam1=beolvasNegativ()
    if szam1 <= 0:
        absolutertek = abs(szam1)
        print("A szám abszolútértéke",szam1)
    else:
        print("A szám nem negatív")

def otodik():
    #Kérj be ellenőrzötten egy 3-mal osztható, kétjegyű számot, majd add meg a négyzetét!
    szam1=beolvasTort()
    if szam1%3==0 and 9<szam1<100:
        print("A szám négyzete:",szam1**2)
    elif szam1%3==0 and -9>szam1>-100:
        print("A szám négyzete:",szam1**2)
    else:
        print("A szám nem osztható hárommal, vagy nem kétjegyű.")






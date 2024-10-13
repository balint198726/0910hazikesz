from random import *
def beolvasEgesz():
    szam = int(input("Kérem adjon meg egy egész számot!"))
    return szam

def beolvasTort():
    szam = float(input("Kérem adjon meg egy valós számot!"))
    return szam

def generalParosEgesz():
        szam1 = randint(-10, 10)
        # print("szám:"+str(szam1))
        while not (szam1 % 2 == 0):
            szam1 = randint(-10, 10)
        return szam1
def beolvasNegativ():
    szam = float(input("Kérem adjon meg egy negatív számot!"))
    return szam

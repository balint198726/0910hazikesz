import math
# from math import pow, pi


def kor():
    # A program olvassa be a konzolról egy kör sugarát! Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kör sugara nem pozitív!"; egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!

    r = float(input("Kérem adjon meg egy kör sugár értéket!"))
    if r>0:
        terulet = r**2 * math.pi
        terulet2 = r*r *math.pi
        terulet3 = math.pow(r, 2) * math.pi
        terulet4 = pow(r, 2)* math.pi
        kerulet = 2 * r * math.pi

        print("A kör területe: "+str(terulet)+", a kör kerülete: "+str(kerulet)+".")
    else:
        print("HIBA: a kör sugara nem pozitív!")

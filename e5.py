def honap():
    # A program  olvasson be a konzolról egy egész számot! Ha a szám 1 és 12 közötti, akkor legyen a beolvasott szám egy hónap sorszáma! A program írja ki a konzolra a sorszámmal megadott hónap nevét! Hiba esetén legyen hibaüzenet!

    szam = int(input("Kérem adjon meg egy hónap sorszámot!"))
    if szam <= 0 or szam >= 13:
        print("HIBA: A megadott zsám nem egy hónap sorszáma!")
    else:
        if szam == 1:
            print("Január.")
        elif szam == 2:
            print("Február.")
        elif szam == 3:
            print("Március.")
        elif szam == 4:
            print("Április.")
        elif szam == 5:
            print("Május.")
        elif szam == 6:
            print("Június.")
        elif szam == 7:
            print("Július")
        elif szam == 8:
            print("Agusztus.")
        elif szam == 9:
            print("Szeptember.")
        elif szam == 10:
            print("Október.")
        elif szam == 11:
            print("November.")
        elif szam == 12:
            print("December.")
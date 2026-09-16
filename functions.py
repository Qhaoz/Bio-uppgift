from classes import Movie, Biljett, Product

movies = [
    Movie("Lord of the Rings", "17:30", "Salong 1", 12),
    Movie("The Matrix", "17:00", "Salong 2", 12),
    Movie("Harry Potter", "16:30", "Salong 3", 0),
    Movie("The Lion King", "16:30", "Salong 4", 0),
    Movie("Saw X", "21:00", "Salong 5", 18)
]


tickets = [
    Biljett("Vuxenbiljett", 100),
    Biljett("Barnbiljett", 50),
    Biljett("Senior", 50)
]


products = [
    Product("Popcorn", 30),
    Product("Baconsnack", 30),
    Product("Läsk", 20),
    Product("Vatten", 10)
]

kundvagn = []


def show_movie():
    print("\n--- FILMER ---")

    try:
        din_alder = int(input("Hur gammal är du? "))
    except ValueError:
        print("felaktig inmatning! Ange din ålder med siffror.")
        return

    print(f"\nVisar filmer för dig som är {din_alder} år:")
    nummer = 1
    hittad = False

    for m in movies:
        if din_alder >= m.aldersgrans:
            print(f"{nummer}, {m.info()}")
            nummer += 1
            hittad = True

    if not hittad:
        print("Det finns inga filmer som passar din ålder.")


def show_biljett():
    print("\n--- BILJETTPRISER ---")
    nummer = 1
    for b in tickets:
        print(f"{nummer}. {b.info()}")
        nummer += 1


def show_product():
    print("\n--- SNACKS & DRYCK ---")
    nummer = 1
    for p in products:
        print(f"{nummer}. {p.info()}")
        nummer += 1


def add_movie():
    print("\n--- LÄGG TILL NY FILM ---")
    titel = input("Ange titel: ")
    tid = input("Ange tid (t.ex. 12:00): ")
    salong = input("Ange salong (t.ex. Salong 0): ")

    try:
        aldersgrans = int(input("Ange åldersgräns (siffra):"))
        ny_film = Movie(titel, tid, salong, aldersgrans)
        movies.append(ny_film)
        print(f"Filmen {titel} har lagts till!")
    except ValueError:
        print("Fel! Åldersgräns måste vara en siffra. Filmen har inte lagts till.")


def search_movie():
    print("\n--- SÖK FILM ---")
    sokord = input("skriv sökord: ").lower()
    hittad = False

    for m in movies:
        if sokord in m.titel.lower():
            print(f"Hittade: {m.info()}")
            hittad = True

    if not hittad:
        print("Ingen film hittades.")


def kassa():
    print("\n--- KASSA ---")

    while True:
        print("\nVad vill du lägga till i kundvagnen?")
        print("1. Vuxenbiljett (100 kr)")
        print("2. Barnbiljett (50 kr)")
        print("3. Seniorbiljett (50 kr)")
        print("4. Popcorn (30 kr)")
        print("5. Baconsnack (30 kr)")
        print("6. Läsk (20 kr)")
        print("7. Vatten (10 kr)")
        print("8. Gå till betalning (Avsluta köp)")

        val = input("Välj (1-8): ")

        if val == "1":
            kundvagn.append(tickets[0])
            print(f"Lade till {tickets[0].namn}!")
        elif val == "2":
            kundvagn.append(tickets[1])
            print(f"Lade till {tickets[1].namn}!")
        elif val == "3":
            kundvagn.append(tickets[2])
            print(f"Lade till {tickets[2].namn}!")
        elif val == "4":
            kundvagn.append(products[0])
            print(f"Lade till {products[0].namn}!")
        elif val == "5":
            kundvagn.append(products[1])
            print(f"Lade till {products[1].namn}!")
        elif val == "6":
            kundvagn.append(products[2])
            print(f"Lade till {products[2].namn}!")
        elif val == "7":
            kundvagn.append(products[3])
            print(f"Lade till {products[3].namn}!")
        elif val == "8":
            break
        else:
            print("ERROR")

    print("\nDina valda varor:")
    if not kundvagn:
        print("Kundvagnen är tom")
        return

    totalt = 0
    for item in kundvagn:
        print(f"- {item.info()}")
        totalt += item.pris

    print(f"Totalt att betala: {totalt} kr")
    input("Tryck ENTER för att genomföra betalning..")
    print("Tack för ditt köp! Njut av filmen!")
    kundvagn.clear()

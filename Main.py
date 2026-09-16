# Minst en egen klass.
# Objekt som skapas från klassen.
# Minst en lista som används för att lagra information eller objekt.
# Flera funktioner eller metoder med tydliga uppgifter.
# Minst en loop.
# Villkor med if, elif och/eller else.
# Användarinmatning med input().
# En meny där användaren kan välja vad programmet ska göra.
# Möjlighet att lägga till information.
# Möjlighet att visa information.
# Möjlighet att söka efter eller hitta information.
# Rimlig hantering av felaktig användarinmatning

# Huvudprogram (Main)
from functions import (
    show_movie,
    show_biljett,
    show_product,
    search_movie,
    add_movie,
    kassa,
)
while True:
    print("\n--- RASMUS-BIO ---")
    print("1. Visa aktuella filmer")
    print("2. Visa biljettpriser")
    print("3. Visa snacks & dryck")
    print("4. Sök film")
    print("5. Lägg till film")
    print("6. Kassa")
    print("7. Exit")

    choice = input("Välj: ")

    if choice == "1":
        show_movie()
    elif choice == "2":
        show_biljett()
    elif choice == "3":
        show_product()
    elif choice == "4":
        search_movie()
    elif choice == "5":
        add_movie()
    elif choice == "6":
        kassa()
    elif choice == "7":
        print("Välkommen åter!")
        break
    else:
        print("ERROR")

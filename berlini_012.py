import requests

BASE_URL = "http://localhost:3001"

try:
    # 1. Cerca Libri di un Autore
    response = requests.get(f"{BASE_URL}/books?author_id=1")
    response.raise_for_status()
    books = response.json()

    print("\nPunto 1: Libri dell'autore con ID 1")
    
    #Fatto per stampare il nome dell'autore
    author_response = requests.get(f"{BASE_URL}/authors/1")
    author_response.raise_for_status()
    author = author_response.json()


    print(f"\nLibri di {author['name']}:")
    for book in books:
        print(f"  - {book['title']} ({book['pages']} pagine)")

    # 2. Filtra per Disponibilità
    
    #versione di chat
    #available_books = [book for book in books if book["available"]]
    
    #versione da verifica
    available_books = []
    for book in books:
        if book["available"]:
            available_books.append(book)

    print("\nPunto 2: Libri disponibili dell'autore con ID 1")

    print("\nLibri disponibili:")
    for book in available_books:
        print(f"  - {book['title']}")

    # 3. Conta Pagine Totali(da quelle trovate disponibili sopra nel punto 2)

    #versione di chat
    #total_pages = sum(book["pages"] for book in available_books)
    
    #versione da verifica
    total_pages = 0
    for book in available_books:
        total_pages += book["pages"]
    
    print("\nPunto 3: Conteggio pagine totali dei libri disponibili")
    print(f"\nPagine totali disponibili: {total_pages}")


    # 4. Libri per Genere

    #Fatto per trovare il numero di libri con genere 101 (Fantasy) trovato dopo con il lenght(len) 
    response = requests.get(f"{BASE_URL}/books?genre_id=101")
    response.raise_for_status()
    fantasy_books = response.json()
    
    #Fatto per stampare il nome del genere
    genre_response = requests.get(f"{BASE_URL}/genres/101")
    genre_response.raise_for_status()
    genre = genre_response.json()

    print("\nPunto 4: Recupero libri di genere Fantasy e stampare quanti numeri sono di quel genere")

    print(f"\nGenere: {genre['name']}")
    print(f"Numero di libri: {len(fantasy_books)}")

except requests.exceptions.RequestException as e:
    print(f"Errore nella richiesta: {e}")
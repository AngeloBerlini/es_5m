import sqlite3

# 2. Connessione: crea il file 'scuola.db' se non esiste
conn: sqlite3.Connection = sqlite3.connect('libreria.db')

# 3. Creazione Cursore
cursor: sqlite3.Cursor = conn.cursor()

def create_tables():

    # 2. Connessione: crea il file 'scuola.db' se non esiste
    conn: sqlite3.Connection = sqlite3.connect('libreria.db')
    # 3. Creazione Cursore
    cursor: sqlite3.Cursor = conn.cursor()

    try:

        # Eseguo DDL per creare la tabella se non esiste

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Autori (
                Id INTEGER PRIMARY KEY,
                Nome TEXT NOT NULL,
                Cognome TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Libri (
                Id INTEGER PRIMARY KEY,
                Titolo TEXT NOT NULL,
                Autore_id INTEGER NOT NULL,
                Anno INTEGER,
                Genere TEXT,
                FOREIGN KEY (Autore_id) REFERENCES Autori(Id)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Prestiti (
                Id INTEGER PRIMARY KEY,
                Libro_id INTEGER NOT NULL,
                Utente TEXT NOT NULL,
                Data_prestito TEXT NOT NULL,
                Data_restituzione TEXT,
                FOREIGN KEY (Libro_id) REFERENCES Libri(Id)
            )
        """)

        conn.commit()
        print("Tabelle create con successo.")


    finally:        # 6. Chiusura Connessione
        conn.close()
    
def insert_data():

    # 2. Connessione: crea il file 'scuola.db' se non esiste
    conn: sqlite3.Connection = sqlite3.connect('libreria.db')
    # 3. Creazione Cursore
    cursor: sqlite3.Cursor = conn.cursor()

    try:
        # 4. Esecuzione Query DML (parametrizzata)
        # Il segnaposto per SQLite è '?'
        cursor.execute(
            "INSERT INTO Autori (Id, Nome, Cognome) VALUES (?, ?, ?)",
            (1, 'Mario', 'Rossi')
        )
        cursor.execute(
            "INSERT INTO Autori (Id, Nome, Cognome) VALUES (?, ?, ?)",
            (2, 'Lucia', 'Bianchi')
        )
        cursor.execute(
            "INSERT INTO Autori (Id, Nome, Cognome) VALUES (?, ?, ?)",
            (3, 'Alessandro', 'Verdi')
        )

        # Inserimento libri
        cursor.execute(
            "INSERT INTO Libri (Id, Titolo, Autore_id, Anno, Genere) VALUES (?, ?, ?, ?, ?)",
            (1, "Il mistero del castello", 1, 2020, "Giallo")
        )
        cursor.execute(
            "INSERT INTO Libri (Id, Titolo, Autore_id, Anno, Genere) VALUES (?, ?, ?, ?, ?)",
            (2, "Viaggio nel tempo", 1, 2018, "Fantascienza")
        )
        cursor.execute(
            "INSERT INTO Libri (Id, Titolo, Autore_id, Anno, Genere) VALUES (?, ?, ?, ?, ?)",
            (3, "La cucina italiana", 2, 2019, "Cucina")
        )
        cursor.execute(
            "INSERT INTO Libri (Id, Titolo, Autore_id, Anno, Genere) VALUES (?, ?, ?, ?, ?)",
            (4, "Storia antica", 3, 2021, "Storia")
        )
        cursor.execute(
            "INSERT INTO Libri (Id, Titolo, Autore_id, Anno, Genere) VALUES (?, ?, ?, ?, ?)",
            (5, "Romanzo moderno", 3, 2022, "Narrativa")
        )
        cursor.execute(
            "INSERT INTO Libri (Id, Titolo, Autore_id, Anno, Genere) VALUES (?, ?, ?, ?, ?)",
            (6,"Il ritorno del castello", 1, 2023, "Giallo")
        )

        # Inserimento prestiti
        cursor.execute(
            "INSERT INTO Prestiti (Id, Libro_id, Utente, Data_prestito, Data_restituzione) VALUES (?, ?, ?, ?, ?)",
            (1, 1, "Mario Rossi", "2023-01-01", "2023-01-15")
        )
        cursor.execute(
            "INSERT INTO Prestiti (Id, Libro_id, Utente, Data_prestito, Data_restituzione) VALUES (?, ?, ?, ?, ?)",
            (2, 2, "Lucia Bianchi", "2023-02-01", None)
        )
        cursor.execute(
            "INSERT INTO Prestiti (Id, Libro_id, Utente, Data_prestito, Data_restituzione) VALUES (?, ?, ?, ?, ?)",
            (3, 3, "Alessandro Verdi", "2023-03-01", "2023-03-10")
        )
        cursor.execute(
            "INSERT INTO Prestiti (Id, Libro_id, Utente, Data_prestito, Data_restituzione) VALUES (?, ?, ?, ?, ?)",
            (4, 4, "Mario Rossi", "2023-04-01", None)
        )

        # 5. Conferma delle modifiche
        conn.commit()

    finally:
        # 6. Chiusura Connessione
        conn.close()

#query_libri_per_autore(autore_id): Restituisce tutti i libri di un autore specifico (usa JOIN).
def query_libri_per_autore(autore_id):
    try:
        # 2. Connessione: crea il file 'scuola.db' se non esiste
        conn: sqlite3.Connection = sqlite3.connect('libreria.db')
        # 3. Creazione Cursore
        cursor: sqlite3.Cursor = conn.cursor()
        
        cursor.execute("SELECT Libri.Titolo, Libri.Anno, Libri.Genere FROM Libri JOIN Autori ON Libri.Autore_id = Autori.Id WHERE Autori.Id = ?", (autore_id,))
        libri = cursor.fetchall()
        return libri

    
    finally:
        # 6. Chiusura Connessione
        conn.close()

   
def query_prestiti_per_utente(utente):
    try:
        # 2. Connessione: crea il file 'scuola.db' se non esiste
        conn: sqlite3.Connection = sqlite3.connect('libreria.db')
        # 3. Creazione Cursore
        cursor: sqlite3.Cursor = conn.cursor()
        
        cursor.execute("SELECT Libri.Titolo, Prestiti.Data_prestito, Prestiti.Data_restituzione FROM Prestiti JOIN Libri ON Prestiti.Libro_id = Libri.Id WHERE Prestiti.Utente = ?", (utente,))
        prestiti = cursor.fetchall()
        return prestiti

    finally:
        # 6. Chiusura Connessione
        conn.close()

    
    
def query_libri_per_genere():
    try:
        # 2. Connessione: crea il file 'scuola.db' se non esiste
        conn: sqlite3.Connection = sqlite3.connect('libreria.db')
        # 3. Creazione Cursore
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("SELECT Genere, COUNT(*) as NumLibri FROM Libri GROUP BY Genere")
        generi = cursor.fetchall()
        return generi  
    finally:
        # 6. Chiusura Connessione
        conn.close()


def query_autori_con_piu_libri():
    try:
        # 2. Connessione: crea il file 'scuola.db' se non esiste
        conn: sqlite3.Connection = sqlite3.connect('libreria.db')
        # 3. Creazione Cursore
        cursor: sqlite3.Cursor = conn.cursor()
        
        cursor.execute("""SELECT Autori.Nome, Autori.Cognome, COUNT(Libri.Id) as NumLibri 
                          FROM Autori 
                          JOIN Libri ON Autori.Id = Libri.Autore_id 
                          GROUP BY Autori.Id 
                          ORDER BY NumLibri DESC""")
        autori = cursor.fetchall()
        return autori  
    finally:
        # 6. Chiusura Connessione
        conn.close()

    
def query_prestiti_non_restituiti():
    try:
        # 2. Connessione: crea il file 'scuola.db' se non esiste
        conn: sqlite3.Connection = sqlite3.connect('libreria.db')
        # 3. Creazione Cursore
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("SELECT Libri.Titolo, Prestiti.Utente, Prestiti.Data_prestito FROM Prestiti JOIN Libri ON Prestiti.Libro_id = Libri.Id WHERE Prestiti.Data_restituzione IS NULL")
        prestiti = cursor.fetchall()
        return prestiti
    finally:
        # 6. Chiusura Connessione
        conn.close()

    
    
    

if __name__ == "__main__":
    create_tables()
    insert_data()
    print("Libri di Mario Rossi:", query_libri_per_autore(1))
    print("Prestiti di Mario Rossi:", query_prestiti_per_utente("Mario Rossi"))
    print("Libri per genere:", query_libri_per_genere())
    print("Autori con più libri:", query_autori_con_piu_libri())
    print("Prestiti non restituiti:", query_prestiti_non_restituiti())
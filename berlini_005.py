import sqlite3

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

    #query_libri_per_autore(autore_id): Restituisce tutti i libri di un autore specifico (usa JOIN).
    print("\n Tutti i libri di Mario rossi")
    cursor.execute("SELECT Libri.Titolo, Libri.Anno, Libri.Genere FROM Libri JOIN Autori ON Libri.Autore_id = Autori.Id WHERE Autori.Nome = ? AND Autori.Cognome = ?", ('Mario', 'Rossi'))
    for libro in cursor.fetchall():
        print(f"Titolo: {libro[0]}, Anno: {libro[1]}, Genere: {libro[2]}")
    
    #query_prestiti_per_utente(utente): Restituisce i prestiti di un utente (usa JOIN).
    print("\n Tutti i prestiti di Mario rossi")
    cursor.execute("SELECT Libri.Titolo, Prestiti.Data_prestito, Prestiti.Data_restituzione FROM Prestiti JOIN Libri ON Prestiti.Libro_id = Libri.Id WHERE Prestiti.Utente = ?", ('Mario Rossi',))
    for prestito in cursor.fetchall():
        print(f"Titolo: {prestito[0]}, Data Prestito: {prestito[1]}, Data Restituzione: {prestito[2]}")

    #query_libri_per_genere(): Restituisce il numero di libri per genere (usa GROUP BY). Assicurati di avere almeno un genere con due libri nell'esempio (per esempio "Giallo" con 2 libri) in modo che la query mostri valori maggiori di 1.
    print("\n Numero di libri per genere:")
    cursor.execute("SELECT Genere, COUNT(*) as NumLibri FROM Libri GROUP BY Genere")
    for genere in cursor.fetchall():
        print(f"Genere: {genere[0]}, Numero di Libri: {genere[1]}")

    #query_autori_con_piu_libri(): Restituisce gli autori ordinati per numero di libri (usa JOIN, GROUP BY, ORDER BY).
    print("\n Autori ordinati per numero di libri:")
    cursor.execute("""SELECT Autori.Nome, Autori.Cognome, COUNT(Libri.Id) as NumLibri 
                      FROM Autori 
                      JOIN Libri ON Autori.Id = Libri.Autore_id 
                      GROUP BY Autori.Id 
                      ORDER BY NumLibri DESC""")
    for autore in cursor.fetchall():
        print(f"Nome: {autore[0]}, Cognome: {autore[1]}, Numero di Libri: {autore[2]}") 
    
    #query_prestiti_non_restituiti(): Restituisce i prestiti non ancora restituiti (data_restituzione IS NULL).
    print("\n Prestiti non ancora restituiti:")
    cursor.execute("SELECT Libri.Titolo, Prestiti.Utente, Prestiti.Data_prestito FROM Prestiti JOIN Libri ON Prestiti.Libro_id = Libri.Id WHERE Prestiti.Data_restituzione IS NULL")
    for prestito in cursor.fetchall():
        print(f"Titolo: {prestito[0]}, Utente: {prestito[1]}, Data Prestito: {prestito[2]}")    
    
    


finally:
    # 6. Chiusura Connessione
    conn.close()
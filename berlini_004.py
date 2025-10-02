import sqlite3

# 2. Connessione: crea il file 'scuola.db' se non esiste
conn = sqlite3.connect('scuola.db')
# 3. Creazione Cursore
cursor = conn.cursor()

try:
    # Eseguo DDL per creare la tabella se non esiste
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Studenti (
            Matricola INTEGER PRIMARY KEY,
            Nome TEXT NOT NULL,
            Cognome TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Esami (
            Id INTEGER PRIMARY KEY,
            Matricola INTEGER NOT NULL,
            Corso TEXT NOT NULL,
            Voto INTEGER,
            FOREIGN KEY (Matricola) REFERENCES Studenti(Matricola)
        )
    """)

    # 4. Esecuzione Query DML (parametrizzata)
    # Il segnaposto per SQLite è '?'
    cursor.execute(
        "INSERT INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)",
        (101, 'Mario', 'Rossi')
    )

    cursor.execute(
        "INSERT INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)",
        (102, "Lucia", "Bianchi")
    )

    # Inserimento esami per studente 101
    cursor.execute(
        "INSERT INTO Esami (Id, Matricola, Corso, Voto) VALUES (?, ?, ?, ?)",
        (1, 101, "Matematica", 28)
    )
    cursor.execute(
        "INSERT INTO Esami (Id, Matricola, Corso, Voto) VALUES (?, ?, ?, ?)",
        (2, 101, "Informatica", 30)
    )
    cursor.execute(
        "INSERT INTO Esami (Id, Matricola, Corso, Voto) VALUES (?, ?, ?, ?)",
        (3, 101, "Fisica", 27)
    )

    # Inserimento esami per studente 102
    cursor.execute(
        "INSERT INTO Esami (Id, Matricola, Corso, Voto) VALUES (?, ?, ?, ?)",
        (4, 102, "Matematica", 28)
    )
    cursor.execute(
        "INSERT INTO Esami (Id, Matricola, Corso, Voto) VALUES (?, ?, ?, ?)",
        (5, 102, "Informatica", 30)
    )
    cursor.execute(
        "INSERT INTO Esami (Id, Matricola, Corso, Voto) VALUES (?, ?, ?, ?)",
        (6, 102, "Fisica", 27)
    )

    # 5. Conferma delle modifiche
    conn.commit()

    # Query 1: Elenco di tutti gli studenti
    print("\nElenco di tutti gli studenti:")
    cursor.execute("SELECT Matricola, Nome, Cognome FROM Studenti")
    for studente in cursor.fetchall():
        print(f"Matricola: {studente[0]}, Nome: {studente[1]}, Cognome: {studente[2]}")

    # Query 2: Elenco dei corsi e voti dello studente con matricola 101
    print("\nEsami sostenuti dallo studente con matricola 101:")
    cursor.execute("SELECT Corso, Voto FROM Esami WHERE Matricola = ?", (101,))
    for esame in cursor.fetchall():
        print(f"Corso: {esame[0]}, Voto: {esame[1]}")

    # Query 3: Numero di esami sostenuti per ciascuno studente
    print("\nNumero di esami per studente:")
    cursor.execute("""
        SELECT s.Matricola, s.Nome, s.Cognome, COUNT(e.Id) as NumEsami
        FROM Studenti s
        LEFT JOIN Esami e ON s.Matricola = e.Matricola
        GROUP BY s.Matricola
    """)
    for riga in cursor.fetchall():
        print(f"Matricola: {riga[0]}, Nome: {riga[1]}, Cognome: {riga[2]}, Numero esami: {riga[3]}")
finally:
    # 6. Chiusura Connessione
    conn.close()
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
            FOREIGN KEY Studenti_matricola REFERENCES Studenti(Matricola)
        )
    """)

    # 4. Esecuzione Query DML (parametrizzata)
    # Il segnaposto per SQLite è '?'
    cursor.execute(
        "INSERT INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)",
        (101, 'Mario', 'Rossi'),
        (102, "Lucia", "Bianchi")
    )

    # 5. Conferma delle modifiche
    conn.commit()

    # Eseguo una SELECT
    cursor.execute("SELECT Nome, Cognome FROM Studenti WHERE Matricola = ?", (101,))
    studente = cursor.fetchone() # I risultati sono tuple
    if studente:
        print(f"Studente trovato (SQLite): {studente} {studente}")

finally:
    # 6. Chiusura Connessione
    conn.close()
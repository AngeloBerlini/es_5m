
CREATE TABLE Beekeper (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
)

CREATE TABLE Typology (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255) NOT NULL,
)   

CREATE TABLE Honey (
    id INT PRIMARY KEY,
    denomination VARCHAR(100) NOT NULL,
    FOREIGN KEY typology_id REFERENCES Typology(id),
)

CREATE TABLE Apiary (
    code VARCHAR(50) PRIMARY KEY,
    num_hives INT NOT NULL,
    locality VARCHAR(100) NOT NULL,
    comune VARCHAR(100) NOT NULL,
    province VARCHAR(100) NOT NULL,
    region VARCHAR(100) NOT NULL,
    beekeeper_id INT NOT NULL,
    FOREIGN KEY (beekeeper_id) REFERENCES Beekeper(id)
)

CREATE TABLE Production (
    id INT PRIMARY KEY,
    year INT NOT NULL,
    quantity FLOAT NOT NULL,
    apiary_code VARCHAR(50) NOT NULL,
    honey_id INT NOT NULL,
    FOREIGN KEY (apiary_code) REFERENCES Apiary(code),
    FOREIGN KEY (honey_id) REFERENCES Honey(id)
)

INSERT INTO Beekeper (id,name) VALUES
(1, "Mario Rossi"),
(2, "Luigi Bianchi"),

INSERT INTO Typology (id,name,description) VALUES
(1, "miele_acacia" , "Il miele di acacia è noto per il suo colore chiaro e il sapore delicato")
(2, "miele_castagno" , "Il miele di castagno ha un colore scuro e un sapore deciso, leggermente amarognolo")

INSERT INTO Honey (id,denomination,typology_id) VALUES
(1, "Miele di Acacia", 1),
(2, "Miele di Castagno", 2);

INSERT INTO Apiary (code,num_hives,locality,comune,province,region,beekeeper_id) VALUES
("Apiario001", 50, "Valle delle Api", "Rovereto", "Trento", "Trentino-Alto Adige", 1),
("Apiario002", 30, "Collina Fiorita", "Arezzo", "Arezzo", "Toscana", 2);

INSERT INTO Production (id,year,quantity,apiary_code,honey_id) VALUES
(1, 2024, 150.5, "Apiario001", 1),
(2, 2025, 80.0, "Apiario002", 2);


SELECT * FROM Beekeper;
SELECT * FROM Typology; 
SELECT * FROM Honey;
SELECT * FROM Apiary;
SELECT * FROM Production;










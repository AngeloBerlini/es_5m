# Esercizio 1

```mermaid
erDiagram




    AZIENDA_VINICOLA {
        int codice_fiscale PK
        str nome
        str via
        int numero_civico
        str comune
        str provincia
        str regione 

    }

    VIGNETI {
        int codice_univoco PK
        str nome
        int superficie_tot
        str località
        str comune
        str classe_esposizione
        str num_filari

    }

    PARCELLE {
        int id PK
        int superficie
        str classe_esposizione

    }

    VITIGNI {
        int id PK
        str nome_scientifico
        str nome_comune
        str colore_bacca
        str origine_genetica
    }



```


I vitigni sono piantati a livello di blocco: per ogni blocco si specifica quali vitigni vi sono coltivati e, per ciascuno, la percentuale della superficie del blocco occupata dal vitigno. Questa struttura permette composizioni diverse tra blocchi dello stesso vigneto.

Le etichette di vino rappresentano l'unità di produzione commerciale: ogni etichetta ha nome, annata e tipologia (es: "DOC", "IGT", "Vino da Tavola"). Un'etichetta è prodotta da un'azienda, proviene da un vigneto principale e può essere associata a un vitigno prevalente.

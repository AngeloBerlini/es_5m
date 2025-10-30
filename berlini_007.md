# Esercizio 7:


```mermaid

erDiagram
    AZIENDA_VINICOLA {
        string partita_iva PK
        string nome
        string via
        int numero_civico
        string comune
        string provincia
        string regione  
    }

    VIGNETI {
        int codice_univoco PK
        string nome
        float superficie_tot
        string localita
        string comune
        string classe_esposizione
        int num_filari
        string partita_iva FK
    }

    PARCELLE {
        int id PK
        float superficie
        string classe_esposizione
        int codice_univoco_vigneto FK
    }

    VITIGNI {
        int id PK
        string nome_scientifico
        string nome_comune
        string colore_bacca
        string origine_genetica
    }

    COLTIVAZIONI {
        int id PK
        int id_parcella FK
        int id_vitigno FK
        float percentuale_superficie
    }

    ETICHETTE {
        int id PK
        string nome
        int annata
        string tipologia
        string partita_iva_produttore FK
        int id_vigneto_principale FK
        int id_vitigno_prevalente FK
    }

    AZIENDA_VINICOLA ||--o{ VIGNETI : possiede
    VIGNETI ||--o{ PARCELLE : e_composto_da
    PARCELLE ||--o{ COLTIVAZIONI : contiene
    VITIGNI ||--o{ COLTIVAZIONI : e_coltivato_in
    AZIENDA_VINICOLA ||--o{ ETICHETTE : produce
    VIGNETI ||--o{ ETICHETTE : fornisce_vigneto_principale
    VITIGNI ||--o{ ETICHETTE : puo_essere_vitigno_prevalente

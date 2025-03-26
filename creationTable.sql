CREATE TABLE Utilisateur (
    id  SERIAL PRIMARY KEY
    nom VARCHAR(50) UNIQUE NOT NULL
    email VARCHAR(250) UNIQUE NOT NULL
    date_inscription TIMESTAMP NOT NOT 
    statut BOOLEAN DEFAULT TRUE
    mot_de_passe TEXT NOT NULL

)

CREATE TABLE Trace_numerique (
    id SERIAL PRIMARY KEY
    utilisateur_id INTEGER REFERENCES Utilisateur(id)
    type_action VARCHAR(100) NOT NULL
    source VARCHAR(100) NOT NULL
    horodatage TIMESTAMP NOT NULL

)

CREATE TABLE Profil (
    id SERIAL PRIMARY KEY
    utilisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE
    pseudo  VARCHAR(50) NOT NULL
    age INTEGER CHECK (age >= 18)
    genre VARCHAR(50) NOT NULL
    orientation VARCHAR(50) NOT NULL
    ville VARCHAR(100) NOT NULL
    pays VARCHAR(100) NOT NULL
    taille NUMERIC(3,1) CHECK (taille >0)
    poids NUMERIC(5,2) CHECK (poids >0)
    bio TEXT

)

CREATE TABLE Match (
    id SERIAL PRIMARY KEY
    utilisateur_id_1 INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE
    utilisateur_id_2 INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE
    date_match TIMESTAMP NOT NULL

)

CREATE TABLE Message(
    id SERIAL PRIMARY KEY
    match_id INTEGER REFERENCES Match(id) ON DELETE CASCADE
    auteur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE
    contenu TEXT NOT NULL
    horodatage TIMESTAMP NOT NULL

)

CREATE TABLE Evenement(
    id SERIAL PRIMARY KEY
    organisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE SET NULL
    titre VARCHAR(255) NOT NULL
    type_evenement VARCHAR(255) NOT NULL
    description TEXT
    lieu VARCHAR(255) NOT NULL
    date_heure TIMESTAMP NOT NULL
    prix NUMERIC(6,2) CHECK (prix >= 0)
)

CREATE TABLE Participation(
    id SERIAL PRIMARY KEY
    utilisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE
    evenement_id INTEGER REFERENCES Evenement(id) ON DELETE CASCADE
    statut VARCHAR(10) CHECK (statut IN ('intéressé','participant'))

)


CREATE TABLE Tag(
    id PRIMARY KEY
    nom VARCHAR(50) UNIQUE NOT NULL

)

CREATE TABLE Tag_evenement(
    evenement_id INTEGER REFERENCES Evenement(id) ON DELETE CASCADE
    tag_id INTEGER REFERENCES Tag(id) ON DELETE CASCADE
    PRIMARY KEY(evenement_id,tag_id)

)


CREATE TABLE Tag_utilisateur(
    utilisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE
    tag_id INTEGER REFERENCES Tag(id) ON DELETE CASCADE
    PRIMARY KEY(utilisateur_id,tag_id)
    
)
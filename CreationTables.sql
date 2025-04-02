CREATE TABLE Utilisateur (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(250) UNIQUE NOT NULL,
    date_inscription TIMESTAMP NOT NULL,
    statut BOOLEAN DEFAULT TRUE,
    mot_de_passe TEXT NOT NULL,
    premium BOOLEAN DEFAULT FALSE
);

CREATE TABLE Trace_Numerique (
    id SERIAL PRIMARY KEY,
    utilisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    type_action VARCHAR(100) NOT NULL,
    source VARCHAR(100) NOT NULL, 
    url TEXT,
    horodatage TIMESTAMP NOT NULL
);

CREATE TABLE Profil (
    utilisateur_id INTEGER PRIMARY KEY REFERENCES Utilisateur(id) ON DELETE CASCADE,
    pseudo VARCHAR(50) NOT NULL,
    age INTEGER CHECK (age >= 18),
    genre VARCHAR(50) CHECK(genre IN ('Homme', 'Femme', 'Non-binaire', 'Autre')),
    orientation VARCHAR(50) CHECK(orientation IN ('Hétérosexuel', 'Homosexuel', 'Bisexuel', 'Asexuel', 'Pansexuel', 'Autre')),
    couleur_yeux VARCHAR(50),
    couleur_cheveux VARCHAR(50),
    origine VARCHAR(50),
    ville VARCHAR(50) NOT NULL,
    pays VARCHAR(50) NOT NULL,
    taille NUMERIC(3,1) CHECK (taille > 0),
    poids NUMERIC(5,2) CHECK (poids > 30),
    bio TEXT,
    nombre_enfant INTEGER DEFAULT 0 CHECK (nombre_enfant >= 0),
    salaire_par_mois NUMERIC(6,2) CHECK (salaire_par_mois >= 0)
);

CREATE TABLE Match (
    id SERIAL PRIMARY KEY,
    utilisateur_id_1 INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    utilisateur_id_2 INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    date_match TIMESTAMP NOT NULL,
    CHECK (utilisateur_id_1 <> utilisateur_id_2)
);

CREATE TABLE Message (
    id SERIAL PRIMARY KEY,
    match_id INTEGER REFERENCES Match(id) ON DELETE CASCADE,
    auteur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    contenu TEXT NOT NULL,
    horodatage TIMESTAMP NOT NULL,
    modifier BOOLEAN DEFAULT FALSE
);

CREATE TABLE Evenement (
    id SERIAL PRIMARY KEY,
    titre VARCHAR(255) NOT NULL,
    type_evenement VARCHAR(255) NOT NULL,
    description TEXT,
    lieu VARCHAR(255) NOT NULL,
    date_heure TIMESTAMP NOT NULL ,
    prix NUMERIC(6,2) CHECK (prix >= 0)
);

CREATE TABLE Participation (
    utilisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    evenement_id INTEGER REFERENCES Evenement(id) ON DELETE CASCADE,
    statut VARCHAR(10) CHECK (statut IN ('intéressé','participant'))
);

CREATE TABLE Presence_Evenement (
    utilisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    evenement_id INTEGER REFERENCES Evenement(id) ON DELETE CASCADE
);

CREATE TABLE Historique_Consultation (
    id SERIAL PRIMARY KEY,
    utilisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    type_contenu VARCHAR(50) CHECK (type_contenu IN ('evenement', 'match', 'profil')),
    url TEXT,
    horodatage TIMESTAMP NOT NULL
);

CREATE TABLE Abonnement (
    id SERIAL PRIMARY KEY,
    utilisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    date_debut TIMESTAMP NOT NULL,
    date_fin TIMESTAMP NOT NULL,
    CHECK (date_fin > date_debut)
);

CREATE TABLE Like (
    id SERIAL PRIMARY KEY,
    utilisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    profil_id INTEGER REFERENCES profil(id) ON DELETE CASCADE,
    type_interaction VARCHAR(10) CHECK (type_interaction IN ('like', 'nope')),
    date_interaction TIMESTAMP NOT NULL,
    annuler BOOLEAN DEFAULT FALSE, 
    CHECK (utilisateur_id <> profil.utilisateur_id)
);

CREATE TABLE Tag (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE Preference_utilisateur (
    utilisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    type_preference VARCHAR(50) REFERENCES,
    valeur_preference INTEGER CHECK (valeur_preference >= 0 AND valeur_preference <= 100),
    PRIMARY KEY (utilisateur_id, type_preference)
);

CREATE TABLE Tag_evenement (
    evenement_id INTEGER REFERENCES Evenement(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES Tag(id) ON DELETE CASCADE,
    PRIMARY KEY (evenement_id, tag_id)
);

CREATE TABLE Tag_Trace_Numerique (
    trace_id INTEGER REFERENCES Trace_Numerique(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES Tag(id) ON DELETE CASCADE,
    PRIMARY KEY (trace_id, tag_id)
);

CREATE TABLE Notification (
    id SERIAL PRIMARY KEY,
    utilisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    type_notification VARCHAR(100),
    message TEXT,
    date_envoi TIMESTAMP NOT NULL,
    vu BOOLEAN DEFAULT FALSE 
);

CREATE TABLE Match_Potentiel (
    id SERIAL PRIMARY KEY,
    utilisateur_id_1 INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    utilisateur_id_2 INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    score_potentiel INTEGER CHECK (score_potentiel >= 0 AND score_potentiel <= 100),
    CHECK (utilisateur_id_1 <> utilisateur_id_2)
);

CREATE TABLE Historique_Match (
    match_id INTEGER PRIMARY KEY REFERENCES Match(id) ON DELETE CASCADE,
    utilisateur_id_1 INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    utilisateur_id_2 INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    date_match TIMESTAMP NOT NULL,
);

CREATE TABLE Consentement (
    utilisateur_id INTEGER PRIMARY KEY REFERENCES Utilisateur(id) ON DELETE CASCADE,
    date_consentement TIMESTAMP NOT NULL
);

CREATE TABLE Organisateur_Evenement (
    utilisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    evenement_id INTEGER REFERENCES Evenement(id) ON DELETE CASCADE
    PRIMARY KEY (utilisateur_id, evenement_id)
);

CREATE TABLE Demande_Suppression (
    id SERIAL PRIMARY KEY,
    utilisateur_id INTEGER REFERENCES Utilisateur(id) ON DELETE CASCADE,
    date_demande TIMESTAMP NOT NULL,
    statut_demande VARCHAR(50) CHECK (statut_demande IN ('en attente', 'acceptée', 'refusée')),
    type_de_donnees VARCHAR(50) CHECK (type_de_donnees IN ('profil', 'trace_numerique', 'historique_match', 'historique_consultation', 'participation', 'presence_événement', 'message', 'organisateur événement', 'tous')),
    date_validation TIMESTAMP 
);


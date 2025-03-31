COPY Utilisateur(nom, prenom, email, date_inscription, statut, mot_de_passe, premium)
FROM './DB/utilisateur.csv'
DELIMITER ','
CSV HEADER;

COPY Profil(utilisateur_id, pseudo, age, genre, orientation, ville, pays, taille, poids, bio)
FROM './DB/profil.csv'
DELIMITER ','
CSV HEADER;

COPY Trace_Numerique(utilisateur_id, type_action, source, url, horodatage)
FROM './DB/trace_numerique.csv'
DELIMITER ','
CSV HEADER;

COPY Match(utilisateur_id_1, utilisateur_id_2, date_match)
FROM './DB/match.csv'
DELIMITER ','
CSV HEADER;

COPY Message(match_id, auteur_id, contenu, horodatage, supprimer)
FROM './DB/message.csv'
DELIMITER ','
CSV HEADER;

COPY Evenement(organisateur_id, titre, type_evenement, description, lieu, date_heure, prix)
FROM './DB/evenement.csv'
DELIMITER ','
CSV HEADER;

COPY Participation(utilisateur_id, evenement_id, statut)
FROM './DB/participation.csv'
DELIMITER ','
CSV HEADER;

COPY Presence_Evenement(utilisateur_id, evenement_id)
FROM './DB/presence_evenement.csv'
DELIMITER ','
CSV HEADER;

COPY Historique_Consultation(utilisateur_id, type_contenu, contenu_id, date_consultation)
FROM './DB/historique_consultation.csv'
DELIMITER ','
CSV HEADER;

COPY Abonnement(utilisateur_id, type_abonnement, date_debut, date_fin)
FROM './DB/abonnement.csv'
DELIMITER ','
CSV HEADER;

COPY Likes(utilisateur_id, profil_id, type_interaction, date_interaction, annuler)
FROM './DB/likes.csv'
DELIMITER ','
CSV HEADER;

COPY Tag(nom)
FROM './DB/tag.csv'
DELIMITER ','
CSV HEADER;

COPY Tag_evenement(evenement_id, tag_id)
FROM './DB/tag_evenement.csv'
DELIMITER ','
CSV HEADER;

COPY Tag_utilisateur(utilisateur_id, tag_id)
FROM './DB/tag_utilisateur.csv'
DELIMITER ','
CSV HEADER;

COPY Tag_Trace_Numerique(trace_id, tag_id)
FROM './DB/tag_trace_numerique.csv'
DELIMITER ','
CSV HEADER;

COPY Notification(utilisateur_id, type_notification, message, date_envoi, vu)
FROM './DB/notification.csv'
DELIMITER ','
CSV HEADER;

COPY Match_Potentiel(utilisateur_id_1, utilisateur_id_2, score_potentiel)
FROM './DB/match_potentiel.csv'
DELIMITER ','
CSV HEADER;

COPY Historique_Match(match_id, utilisateur_id_1, utilisateur_id_2, date_match)
FROM './DB/historique_match.csv'
DELIMITER ','
CSV HEADER;

COPY Preference_utilisateur(utilisateur_id, type_preference, valeur_preference)
FROM './DB/preference_utilisateur.csv'
DELIMITER ','
CSV HEADER;

COPY Consentement(utilisateur_id, type_consentement, date_consentement)
FROM './DB/consentement.csv'
DELIMITER ','
CSV HEADER;

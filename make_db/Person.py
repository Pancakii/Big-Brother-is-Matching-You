import csv
import os
from random import randint, choice


class Person:
    total = 0
    files = []
    pseudos = []

    def __init__(self):
        # utilisateur
        self.nom = ""
        self.prenom = ""
        self.email = ""
        self.date_inscription = ""
        self.statut = choice([True, False])
        self.mot_de_passe = ""
        self.premium = choice([True, False])

        # profil
        self.pseudo = ""
        self.age = 0
        self.genre = ""
        self.orientation = ""
        self.ville = ""
        self.pays = ""
        self.taille = 140
        self.poids = 50
        self.bio = ""

        if self.init_person():
            Person.total += 1

    def init_person(self):
        while len(Person.files) > 0:
            if len(Person.files[0]) == 0:
                Person.files.pop(0)
                continue
            # to fix: pseudo, orientation and maybe bio
            # prenom,nom,email,status,mot_de_passe,premium,pseudo,age,gender,orientation,ville,pays,taille,poids,bio
            whole_data = Person.files[0].pop(0)
            [self.prenom, self.nom, self.email,
             self.statut, self.mot_de_passe, self.premium,
             self.pseudo, self.age, self.genre,
             self.orientation, self.ville, self.pays,
             self.taille, self.poids, self.bio] = whole_data
            return True
        print("Error while initializing person: Not enough data.")
        return False

    def get_pseudo(self):
        if len(Person.pseudos) == 0:
            print("No pseudos left")
        else:
            self.pseudo = Person.pseudos.pop(randint(0, len(self.pseudos) - 1))

    def get_orientation(self):
        num = randint(1, 100)
        percs = [80, 90, 100]
        res = ["heterosexual", "homosexual", "bisexual"]
        for i in range(len(percs)):
            if num <= percs[i]:
                self.orientation = res[i]
                return

        self.orientation = "Hetero"

    def get_bio(self):
        length = randint(32, 64)
        self.bio = ""
        for i in range(length):
            self.bio += chr(randint(97, 122))

    def get_user_str(self):
        res = ','.join([self.nom, self.prenom, self.email,
                        self.date_inscription, str(self.statut),
                        self.mot_de_passe, str(self.premium)])
        """
        # utilisateur
        self.nom = ""
        self.prenom = ""
        self.email = ""
        self.date_inscription = []
        self.statut = choice([True, False])
        self.mot_de_passe = ""
        self.premium = choice([True, False])
        """
        return res

    def get_profile_str(self):
        return


    @staticmethod
    def get_pseudos(length):
        """
        Get nicknames in a list for pseudos
        :param length: length of nicknames wanted
        :return: nothing
        """

        res = []
        with open("nickname/hypixel-players.txt", 'r') as f:
            for line in f:
                if length <= 0:
                    break
                line = line.strip()
                res.append(line)
                length -= 1

        Person.pseudos = res

    @staticmethod
    def get_files():
        liste = os.listdir("mock_data")
        for file in liste:
            if file.endswith(".csv"):
                try:
                    Person.files.append([])
                    f = open(file, 'r', encoding='utf-8')
                    reader = csv.reader(f)
                    next(reader)
                    # Get the whole file in the list
                    for line in reader:
                        Person.files[-1].append(line)
                    f.close()
                except Exception as e:
                    print(f"Passing file {file}. " + str(e))

    @staticmethod
    def make_db(length):
        """
        Makes Utilisateur and Profil db
        :return: nothing
        """
        Person.get_files()
        Person.get_pseudos(length)
        uf = open("utilisateur.csv", 'w', encoding='utf-8')
        pf = open("profile.csv", 'w', encoding='utf-8')
        while Person.total < length:
            person = Person()
            if person.nom == "":
                print(f"Somehow Person nom is empty. Stopping generating. People made: {Person.total}")
                break



if __name__ == "__main__":
    print("Done")

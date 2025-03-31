#!/usr/bin/env python3
"""
Profil:
id (pour numerer, ignorable)
#utilisateur_id (random?)
age
genre (sex?)
orientation (jsp quoi mettre)
ville
pays
taille (140-210)
poids (50-150)
bio (jsp quoi mettre)
"""
import sys
from random import choice, randint
import csv


def get_random_from_list(liste, n):
    res = []
    for i in range(n):
        try:
            element = choice(liste)
            res.append(element)
            liste.remove(element)
        except:
            print(f"Number entered is too big, putting the whole list in the file. Length: {len(liste)}")
            return liste

    return res


def get_country_city(filename, n):
    """
    Get country and city in a list from filename
    :param filename: file name
    :param n: number of country and city couples
    :return: list of (country, city)
    """
    whole_file = []

    f = open(filename, 'r', encoding='utf-8')
    reader = csv.reader(f)
    next(reader)
    # Get the whole file in the
    for line in reader:
        country = line[4].strip()
        city = line[1].strip()
        whole_file.append((country, city))

    f.close()

    return get_random_from_list(whole_file, n)


def get_bio(_unused):
    length = randint(16, 64)
    res = ""
    for i in range(length):
        res += chr(randint(97, 122))
    return res


def get_poids(_unused):
    return str(randint(50, 150))


def get_taille(_unused):
    return str(randint(140, 210))


def get_age(_unused):
    return str(randint(18, 40))


def get_gender(_unused):
    return choice(['male', 'female'])


def get_orientation(_unused):
    num = randint(1, 100)
    percs = [90, 95, 100]
    res = ["heterosexual", "homosexual", "bisexual"]
    for i in range(len(percs)):
        if num <= percs[i]:
            return res[i]

    return "Hetero"


def get_with_proba(string, proba, maxi):
    if randint(1, maxi) <= proba:
        return "," + string
    return ","


def get_couple_cc(liste):
    els = liste.pop()
    return els[0].strip() + "," + els[1].strip()


def write_profile_file(length, output_f, is_production=False):
    if is_production:
        output_f = r"../DB/" + output_f
    with open(output_f, 'w', encoding='utf-8') as f:
        country_city = get_country_city("country_city/worldcities.csv", length)

        funcs = [get_age, get_gender, get_orientation, get_couple_cc, get_taille, get_poids, get_bio]
        params = [None, None, None, length, None, None, None]
        percs = [(8, 10), (1, 1), (1, 1), (1, 1), (8, 10), (8, 10), (7, 10)]
        while len(country_city) > 0:
            """
            age = get_age() # NULLABLE
            gender = get_gender()
            orientation = get_orientation()
            cv = country_city.pop()
            country = cv[0]
            city = cv[1]
            taille = get_taille() # NULLABLE
            poids = get_poids()  # NULLABLE
            bio = get_bio() # NULLABLE
            """
            line = ""

            for i in range(len(funcs)):
                line += get_with_proba(funcs[i](params[i]), percs[i][0], percs[i][1])

            # Get rid of the first "," and add \n to the end
            line = line[1:] + "\n"

            f.write(line)


if __name__ == '__main__':
    # Check the arguments
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print('Usage: %s <length of the database> <output file name> <is for production=0(1 = yes, 0 = no)>' % sys.argv[0])
        sys.exit(1)

    # Get the length of the database
    try:
        num = int(sys.argv[1])
        if len(sys.argv) == 4:
            is_production = bool(int(sys.argv[3]))
        else:
            is_production = False
    except ValueError:
        print('Usage: %s <length of the database> <output file name> <is for production=0(1 = yes, 0 = no)>' % sys.argv[0])
        sys.exit(1)

    # Get output file name
    output_file_name = sys.argv[2]

    write_profile_file(num, output_file_name, is_production)

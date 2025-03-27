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


def get_nickname(filename, n):
    """
    Get random nicknames in a list from filename
    :param filename: file name
    :param n: number of nicknames
    :return: list of nicknames
    """

    nicknames = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            nicknames.append(line)

    return get_random_from_list(nicknames, n)


def get_country_city(filename, n):
    """
    Get country and city in a list from filename
    :param filename: file name
    :param n: number of country and city couples
    :return: list of (country, city)
    """
    whole_file = []

    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()
    lines.pop(0)
    # Get the whole file in the
    for line in lines:
        line_format = line.split(',')
        country = line_format[4].strip()
        city = line_format[1].strip()
        whole_file.append((country, city))

    f.close()

    return get_random_from_list(whole_file, n)


def get_bio():
    length = randint(16, 64)
    res = ""
    for i in range(length):
        res += chr(randint(97, 122))
    return res


def get_poids():
    return randint(50, 150)


def get_taille():
    return randint(140, 210)


def get_age():
    return randint(18, 40)


def get_gender():
    return choice(['male', 'female'])


def get_orientation():
    num = randint(1, 100)
    percs = [90, 95, 100]
    res = ["heterosexual", "homosexual", "bisexual"]
    for i in range(len(percs)):
        if num <= percs[i]:
            return res[i]

    return "Hetero"


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


def write_file(country_city, output_file_name):
    with open(output_file_name, 'w', encoding='utf-8') as f:
        id = 1
        while len(country_city) > 0:
            """
            id
            user_id
            age = get_age()
            gender = get_gender()
            orientation = get_orientation()
            cv = country_city.pop()
            country = cv[0]
            city = cv[1]
            taille = get_taille()
            poids = get_poids()
            bio = get_bio()
            """
            line = [str(id), str(id), str(get_age()), get_gender(), get_orientation()]
            cv = country_city.pop()
            if cv is None:
                continue
            line.append(cv[0])
            line.append(cv[1])
            line = line + [str(get_taille()), str(get_poids())]

            line = ','.join(line)

            line = line + ","

            if randint(0, 10) < 7:
                line = line + get_bio()

            line = line + "\n"

            f.write(line)
            id += 1


if __name__ == '__main__':
    # Check the arguments
    if len(sys.argv) != 3:
        print('Usage: %s <length of the database> <output file name>' % sys.argv[0])
        sys.exit(1)

    # Get the length of the database
    try:
        num = int(sys.argv[1])
    except ValueError:
        print('Usage: %s <length of the database> <output file name>' % sys.argv[0])
        sys.exit(1)

    # Get output file name
    output_file_name = sys.argv[2]

    # Get the nickname list
    #nicknames = get_nickname("nickname/hypixel-players.txt", num)
    country_city = get_country_city("country_city/worldcities.csv", num)

    write_file(country_city, output_file_name)

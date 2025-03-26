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
from random import choice




def get_random_from_list(liste, n):
    res = []
    for i in range(n):
        try:
            element = liste.remove(choice(liste))
            res.append(element)
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

    f = open(filename, 'r')
    lines = f.readlines()
    lines.remove(lines[0])
    # Get the whole file in the
    for line in lines:
        line = line.strip()
        line_format = line.split(',')
        country = line_format[4].strip()
        city = line_format[1].strip()
        whole_file.append((country, city))

    f.close()

    return get_random_from_list(whole_file, n)





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

    # Get the nickname list
    nicknames = get_nickname("nickname/hypixel-players.txt", num)
    country_city = get_country_city("country_city/worldcities.csv", len(nicknames))
    





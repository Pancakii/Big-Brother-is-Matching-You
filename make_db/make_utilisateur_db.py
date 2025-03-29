#!/usr/bin/env python3
"""
Utilisateur:
nom NOT NULL
email NOT NULL
date d'inscription (format?)
statut (true/false) (actif ou pas)
mot de passe NOT NULL
"""
import sys
from random import choice, randint


def get_random_from_list(liste):
    if len(liste) > 0:
        element = choice(liste)
        res = element
        liste.remove(element)
        return res
    else:
        return ""


def get_nicknames(filename, length):
    """
    Get random nicknames in a list from filename
    :param filename: file name
    :return: list of nicknames
    """

    res = []
    with open(filename, 'r') as f:
        for line in f:
            if length <= 0:
                break
            line = line.strip()
            res.append(line)
            length -= 1

    return res


def get_rand_str(minmax):
    length = randint(minmax[0], minmax[1])
    res = ""
    for i in range(length):
        res += chr(randint(97, 122))
    return res


def get_email(_unused):
    # TODO: FIX THIS IF YOU WANT SMTH REALISTIC
    res = get_rand_str((6, 12))
    res += "@" + choice(["hotmail", "gmail"]) + ".com"
    return res


def get_date(_unused):
    rmonth = randint(1, 12)
    if rmonth != 2:
        if rmonth in [1, 3, 5, 7, 8, 10, 12]:
            rday = randint(1, 31)
        else:
            rday = randint(1, 30)
    else:
        rday = randint(1, 28)
    rday = str(rday)
    rmonth = str(rmonth)
    ryear = str(randint(2015, 2025))
    return "-".join([rday, rmonth, ryear])


def get_status(_unused):
    return "true" if randint(1, 10) < 8 else "false"


def get_with_proba(string, proba, maxi):
    if randint(1, maxi) <= proba:
        return "," + string
    return ","


def write_file(length, output_f, is_pd=False):
    if is_pd:
        output_f = r"../DB/" + output_f
    with open(output_f, 'w', encoding='utf-8') as f:
        nicknames = get_nicknames("nickname/hypixel-players.txt", length)

        funcs = [get_random_from_list, get_email, get_date, get_status, get_rand_str]
        params = [nicknames, None, None, None, (8, 16)]
        percs = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]
        while len(nicknames) > 0:
            """
            Utilisateur:
            nom NOT NULL
            email NOT NULL
            date d'inscription (format?)
            statut (true/false) (actif ou pas)
            mot de passe NOT NULL
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

    write_file(num, output_file_name, is_production)

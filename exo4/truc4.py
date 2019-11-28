# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/


def get_pierre(input: list, n):
    liste = []
    for line in input[1:n + 1]:
        l = line.split()
        liste.append({
            'valeur': int(l[0]),
            'poids': int(l[1])
        })
    return liste


def get_poudres(input: list, n, m):
    liste = []
    for line in lines[n + 1:n + m + 1]:
        l = line.split()
        liste.append({
            'prix/poids': int(l[0]),
            'quantité_dispo': int(l[1])
        })
    return liste


if __name__ == "__main__":
    index = 2
    with open("input{}.txt".format(index), "r") as file:
        lines = file.read().split("\n")
    with open("output{}.txt".format(index)) as file:
        output = file.read().split("\n")

    line_1 = lines[0].split()
    line_1 = [int(line) for line in line_1]
    nb_type_pierres = line_1[0]
    nb_type_poudre = line_1[1]
    max_contenance = line_1[2]

    pierres_desc = get_pierre(lines, nb_type_pierres)
    poudres_desc = get_poudres(lines, nb_type_pierres, nb_type_poudre)

    pierres_desc = sorted(pierres_desc, key=lambda x: x['valeur'], reverse=True)
    poudres_desc = sorted(poudres_desc, key=lambda x: x['prix/poids'], reverse=True)

    max_values_pierre = []
    max_contenance_pierre = []
    sac_contenance = 0
    for i in pierres_desc:
        max_value = 0
        sac_contenance = 0
        while sac_contenance < max_contenance:
            max_value += i['valeur']
            sac_contenance += i['poids']
        max_values_pierre.append(max_value)
        max_contenance_pierre.append(sac_contenance)

    for i in poudres_desc:
        while sac_contenance < max_contenance:
            if i['quantité_dispo'] <= 0:
                break
            max_value += i['prix/poids']
            sac_contenance += 1
            i['quantité_dispo'] -= 1

    pass

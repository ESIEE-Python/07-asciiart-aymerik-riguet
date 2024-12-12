"""code permettant d'utiliser les tuples sur des élément ascii"""
#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(1500)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en arg algo iteratif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    c = [s[0]]
    o = [1]
    s = s[1 :]
    k = 0
    n = len(s)
    while k < n :
        if s[k] == s[k-1]:
            o[-1] += 1
        else :
            c.append(s[k])
            o.append(1)
        k += 1
    return list(zip(c, o))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en arg algo récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    # Trouver le nombre d'occurrences consécutives du premier caractère
    o = 1
    while o < len(s) and s[o] == s[0]:
        o += 1
    # Construire la liste avec l'appel récursif
    return [(s[0], o)] + artcode_r(s[o:])
#### Fonction principale
def main():
    """test les méthode crée"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))
    print(artcode_i('AArrrbbrrree'))
    print(artcode_r('AArrrbbrrree'))
    print(artcode_i('EESSSSSSIEEE'))
    print(artcode_r('EESSSSSSIEEE'))

if __name__ == "__main__":
    main()

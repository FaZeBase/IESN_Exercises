"""
Cette fonction renvoie la racine carée d'un nombre réel mis en paramètre
Arguments : square_root(nb1: int) -> float
                        ^              ^
                        |               - résultat
                        |
                         - nombre à mettre en racine carée
"""
def square_root(nb: int) -> float :
    return nb  ** (0.5)
print(square_root(9))

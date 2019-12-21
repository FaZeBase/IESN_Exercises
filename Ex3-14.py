"""
Cette fonction calcule l'aire d'un cercle dont le rayon est mis en paramètres
Arguments : circle_area(nb1: float) -> float
                         ^               ^
                         |                - aire
                         |    
                          - rayon
"""
import math
def circle_area(radius: float) -> float :
    return math.pi * radius ** 2.0
print(circle_area(3.0))

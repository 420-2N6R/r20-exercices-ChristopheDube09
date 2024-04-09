from math import pi
#1. Ajouter un raise Exception qui lèvera une exception de type TypeError si le type de paramètre passé
#        lors du __init__ n’est pas un int ou float ( vous pouvez utiliser la fonction type() )

#2.	Ajouter un raise Exception qui lèvera une exception de type ValueError  si la valeur du rayon est 
#       égale ou inférieure à 0

#3.	Terminer la propriété rayon

#4.	Ajouter un setter à la propriété rayon. Le setter doit faire les mêmes vérifications que dans 
#       le __init__ afin de s’assurer que le rayon est correct.

#5.	Terminer les propriétés, circonférence, volume et aire qui ont déjà été déclarés dans la classe.
#       (NOTEZ : la valeur de pi à été importer, vous pouvez utilisé pi comme une constante)




class Sphere:
    def __init__(self, pRayon) -> None:
        self._rayon = pRayon
        if not isinstance(pRayon, (int, float)):
            raise TypeError("Le rayon doit être un entier ou un flottant.")
        if pRayon <= 0:
            raise ValueError("Le rayon doit être supérieur à 0.")
        self._rayon = pRayon
    @property
    def rayon(self,value) :
        if not isinstance(value, (int, float)):
            raise TypeError("Le rayon doit être un entier ou un flottant.")
        if value <= 0:
            raise ValueError("Le rayon doit être supérieur à 0.")
        
        self._rayon = value

    @property
    def circonference(self):
        return 2 * pi * self._rayon

    @property
    def volume(self):
        return (4/3) * pi * (self._rayon ** 3)

    @property
    def aire(self):
        return 4 * pi * (self._rayon ** 2)


if __name__ == "__main__" :
    print(pi)  # Vous pouvez utiliser la constante pi

    # Testez votre code
    try:
        sph = Sphere("texte")
    except TypeError as e:
        print(e)  # Affiche : Le rayon doit être un entier ou un flottant.

    try:
        sph = Sphere(-2)
    except ValueError as e:
        print(e)  # Affiche : Le rayon doit être supérieur à 0.

    sph = Sphere(5)  # Crée une sphère avec un rayon de 5
    print("Rayon:", sph.rayon)
    print("Circonférence:", sph.circonference)
    print("Volume:", sph.volume)
    print("Aire:", sph.aire)


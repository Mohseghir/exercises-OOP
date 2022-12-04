'''
class Bird:
    """oiseau"""
    def __init__(self):
        """on definis ici les attributs d'instance"""
        self.wings = 2
    def fly(self):
        """une méthode d'instance"""
        print("je vole!")
bird = Bird()  # obligation d'instancier un oiseau pour utlisier ses attributs
bird.wings
bird.fly()
'''


class Bird:
    """un oiseau"""
    # ici on utilise deux attributs de classe
    names = ("mouette", "pigeon", "moineau", "hirrondelle")
    positions = {}

    def __init__(self, name):
        """les attributs définis ici sont des attributs d'instance"""
        self.position = 1, 2
        self.name = name

        # on accède à l'attribut de classe "positions" avec self (c'est possible)
        self.positions[self.position] = self.name

    @classmethod
    def find_bird(cls, position):
        """retrouve un oiseau selon la position donnée"""
        if position in cls.positions:
            return f"on a trouvé un {cls.positions[position]}"

        return "on a rien trouvé"

    @staticmethod
    def get_definition():
        """Donne la définition d'un oiseau"""
        return (
            "animal bla blabla"
        )


print(Bird.get_definition())

# On peut accéder aux variables de classe sans instanciantion
Bird.names
Bird.positions
print(Bird.find_bird((2, 5)))

# on instancie un oiseau
bird = Bird("mouette")

# on le retrouve avec la méthode find_bird.
print(Bird.find_bird((1, 2)))

# je n'ai pas compris le code ci-dessus################################

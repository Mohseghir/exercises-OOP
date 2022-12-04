"""Définit des classes d'outils."""


class ToolBox:
    """Boite à outils."""

    def __init__(self):
        """Initialise les outils."""
        self.tools = []

    def add_tool(self, tool):
        """Ajoute un outil."""
        self.tools.append(tool)

    def remove_tool(self, tool):
        """Enleve un outil."""
        index = self.tools.index(tool)
        del self.tools[index]


class Screwdriver:
    """Tournevis."""

    def __init__(self, size=3):
        """Initialise la taille."""
        self.size = size

    def tighten(self, screw):
        """Serrer une vis."""
        screw.tighten()

    def loosen(self, screw):
        """Desserre une vis."""
        screw.loosen()

    def __repr__(self):
        """Représentation de l'objet"""
        return f"Tournevis de taille {self.size}"


class Hammer:
    """Marteau."""

    def __init__(self, color="red"):
        """Initialise la couleur."""
        self.color = color

    def paint(self, color):
        """Paint le marteau."""
        self.color = color

    def hammer_in(self, nail):
        """Enfonce un clou."""
        nail.nail_in()

    def remove(self, nail):
        """Enleve un clou."""
        nail.remove()

    def __repr__(self):
        """Représentation de l'objet"""
        return f"marteau de couleur {self.color}"


class Screw:
    """vis"""
    MAX_TIGHTNESS = 5

    def __init__(self):
        """Initialise son degré de serrage"""
        self.tightness = 0

    def loosen(self):
        """déserre le vis"""
        if self.tightness > 0:
            self.tightness -= 1

    def tighten(self):
        """serre le vis"""
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1

    def __str__(self):
        """retourne une fomre lisible de l'objet"""
        return "Vis avec un serrage de {}".format(self.tightness)


class Nail:
    """Clou"""

    def __init__(self):
        """initialise son statut "dans le mur"."""
        self.in_wall = False

    def nail_in(self):
        """Enfonce le clou dans unb mur"""
        if not self.in_wall:
            self.in_wall = True

    def remove(self):
        """enlève le clou du mur """
        if self.in_wall:
            self.in_wall = False

    def __str__(self):
        """retourne une forme lisible de l'objet"""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}"


# instanciez les objets : boite à outil, tournevis et marteau

toolbox = ToolBox()
screwdriver = Screwdriver()
hammer = Hammer()


# placer le marteau et le tourne vis dans le caisse

toolbox.add_tool(screwdriver)
toolbox.add_tool(hammer)

#instanciez une vis et la serrer puis l'afficher avant et apres

screw = Screw()
print(screw)
screwdriver.tighten(screw)
print(screw)

# instancier un clou et l'enfoncer avec le marteau

nail = Nail()
hammer.hammer_in(nail)
print(nail)
hammer.remove(nail)
print(nail)

# retirer le marteau de la caisse

print("outil dans la caisse:", toolbox.tools)
toolbox.remove_tool(hammer)
print("on a elevé le marteau")
print("outil dans la caisse:", toolbox.tools)

# desseer la vis

print("la vis est serré à :", screw.tightness)
# screw.loosen()
screwdriver.loosen(screw)
print("la vis est serré à :", screw)

# retirer un coul

hammer.remove(nail)
print(nail)

# rependre le marteau

hammer.paint("bleu")
print(hammer)

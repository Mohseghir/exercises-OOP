class Film:
    def __init__(self, name):
        self.name = name

    def watch(self):
        print("bon visionnage !")


class FilmCassette(Film):
    def __init__(self, name):
        """initialise le nom et la bande magnétique """
        self.name = name
        self.magnetic_tape = True

    def rewind(self):
        """rembobiner le film"""
        print("ça rembobine !")
        self.magnetic_tape = True


film = Film("2001: l'odyssée de l'espace")
filmCassette = FilmCassette("Blade Runner")


class FilmDvd(Film):  # sous class de Film
    pass


filmdvd = FilmDvd("matrix")


class FilmBlueRay(Film):
    pass


filmblueray = FilmBlueRay("titanic")

print(film.name)
film.watch()

print(filmCassette.name)
print(filmCassette.magnetic_tape)
filmCassette.watch()
filmCassette.rewind()

print(filmdvd.name)
filmdvd.watch()

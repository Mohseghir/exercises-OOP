# exo mettre les élément d'un site de forum en class :

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        """affichage du fichier"""
        print(f"Fichier '{self.name}'")


class Image(File):
    pass

class User:
    """iniitialisation utilisateur"""
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        """connection"""
        print(f"l'utilisateur {self.username} est connecté.")
# je n'ai pas compris le code qui suit
    def post(self, thread, content, file=None):
        """poster un message dans un thread"""
        if file:
            post = FilePost(self, "aujourd'hui", content, file)
        else:
            post = Post(user=self, time_posted="aujourd'hui", content=content)
        thread.add_post(post)
        return post
    def make_thread(self, title, content):
        """crée un nouveau fil de discussion"""
        post = Post(self, "aujourd'hui", content)
        return Thread(title, "aujoud'hui", post)
    def __str__(self):
        """representation du user"""
        return self.username


class Moderator(User):
    """utilisateur modérateur"""

    def edit(self, post, content):
        """modifier un message"""
        post.content = content

    def delete(self, thread, post):
        """supprime un message"""
        index = thread.posts.index(post)
        del thread.posts[index]

class Post:
    """message"""
    def __init__(self, user, time_posted ,content):
        """initialiser l'utilisateur, la date et le contenu."""
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        """affiche le message"""
        print(f"message posté par {self.user} le {self.time_posteda}:")
        print(self.content)

class FilePost(Post):
    """Mesaage avec un fichier"""

    def __init__(self, user, time_posted, content, file):
        """initialiser les fichier"""
        self.user = user
        self.time_posted = time_posted
        self.content = content
        self.file = file

    def display(self):
        """Affiche le contenu et le fichier"""
        super().display()
        print("piéce jointe")
        self.file.display()


class Thread:

    def __init__(self, title, time_posted, post):
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]

    def display(self):
        """afficher le fil de discution"""
        print("----THREAD---")
        print(f"titre: {self.titre}, date: {self.time_posted}")
        print()
        for post in self.posts:
            post.display()
            print()
        print("-------------")

    def add_post(self, post):
        """"Ajoute un post"""
        self.posts.append(post)

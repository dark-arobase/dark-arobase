class Utilisateur():

    def __init__(self, id, username, email, password, liste_publications):
        # TODO: Ajouter les autres attributs nécessaires
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.liste_publications = liste_publications

    def __str__(self):
        return f"Utilisateur(id={self.id}, username='{self.username}')"
    
    

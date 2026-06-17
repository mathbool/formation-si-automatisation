
class LecteurDonnees:

    def __init__(self):
        self.liste_de_dicts = []

    def charger(self, source):
        #print (source)
        for elem in source:
            self.liste_de_dicts.append(elem)
        return self.liste_de_dicts


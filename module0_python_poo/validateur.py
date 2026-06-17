from datetime import datetime

class PrixInvalideError(Exception):
    pass

class QuantiteManquanteError(Exception):
    pass

class CodeArticleError(Exception):
    pass

class Validateur():

    def __init__(self):
        self.liste_de_lignes = []
        self.file_rapport = r"C:\Users\GET\3D Objects\Project\Perso\Fiches d'exercies\Solutions\formation-si-automatisation\module0_python_poo\rapport.txt"
        #{code: xxx, "prix": 0, "quantite": 0}

    def valider_fichier(self):
        with open(self.file_rapport, "w", encoding="utf-8") as f:
            for i, ligne in enumerate(self.liste_de_lignes,1):
                f.write(f"{i} - {datetime.now()} - {ligne}\n")
                print(f"{i} - {datetime.now()} - {ligne}")
        print(f"Enregistrement effectué dans :\n'{self.file_rapport}'")

    def valider_ligne(self, donnees_dict):
        self.donnees_dict = donnees_dict
        try:
            ligne_valide = self._valide_ligne()
            self.liste_de_lignes.append(ligne_valide)
        except (PrixInvalideError, QuantiteManquanteError, CodeArticleError) as e:
            self.liste_de_lignes.append(f"Erreur : {e}")

    def _valide_ligne(self):
        erreur = ""
        for cle, valeur in self.donnees_dict.items():
            match cle:
                case "prix":
                    if valeur <= 0:
                        erreur = "Prix non valide !"
                        raise PrixInvalideError(erreur)
                case "quantite":
                    if type(valeur) == int:
                        if valeur <= 0:
                            erreur = "Quantité invalide !"
                            raise QuantiteManquanteError(erreur)
                case "code_produit":
                    if not str(valeur).startswith("ART-") or len(valeur) != 8:
                        erreur = "Format code incorrecte : ART-XXXX"
                        raise CodeArticleError(erreur)   
        return self.donnees_dict if erreur == "" else erreur
    




v= Validateur()
p1 = {"code_produit" : "ART-123A", "prix": 250, "quantite" : 2}
p2 = {"code_produit" : "ART-223A", "prix": 250, "quantite" : 0}
p3 = {"code_produit" : "ART-323A", "prix": -52, "quantite" : 2}
p4 = {"code_produit" : "ART-423A", "prix": 250, "quantite" : 2}
p5 = {"code_produit" : "ART-523hA", "prix": 250, "quantite" : 2}

v.valider_ligne(p1)
v.valider_ligne(p2)
v.valider_ligne(p3)
v.valider_ligne(p4)
v.valider_ligne(p5)

v.valider_fichier()
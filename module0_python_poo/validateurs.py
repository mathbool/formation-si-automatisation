from exceptions import CodeArticleError, PrixInvalideError, QuantiteManquanteError

class Validateur():

    def __init__(self):
        self.liste_de_lignes = []        
        #{code: xxx, "prix": 0, "quantite": 0}

    def valider_fichier(self):
        #with open(self.file_rapport, "w", encoding="utf-8") as f:
        #    for i, ligne in enumerate(self.liste_de_lignes,1):
        #        f.write(f"{i} - {datetime.now()} - {ligne}\n")
        #        print(f"{i} - {datetime.now()} - {ligne}")
        #print(f"Enregistrement effectué dans :\n'{self.file_rapport}'")
        return self.liste_de_lignes

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
    
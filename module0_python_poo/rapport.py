from validateurs import Validateur as v
from datetime import datetime

class Rapport :

    def __init__(self, donnees):
        self.file_rapport = r"C:\Users\GET\3D Objects\Project\Perso\Fiches d'exercies\Solutions\formation-si-automatisation\module0_python_poo\rapports.txt"
        self.liste_de_lignes = donnees
        
    def rapport(self):
        #d = v.valider_fichier() 
        with open(self.file_rapport, "w", encoding="utf-8") as f:
            for i, ligne in enumerate(self.liste_de_lignes,1):
                f.write(f"{i} - {datetime.now()} - {ligne}\n")
                print(f"{i} - {datetime.now()} - {ligne}")
        print(f"Enregistrement effectué dans :\n'{self.file_rapport}'")

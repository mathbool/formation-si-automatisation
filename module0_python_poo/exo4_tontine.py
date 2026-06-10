
class Membre:

    def __init__(self, nom, telephone): #historique_cotisations = []):
        self.nom = nom
        self.telephone = telephone
        self.historique_cotisations = {
            "janvier" : []
        }
        self.separation = "|"
        self.montant = 0
        
    def cotiser(self, mois): #ajoute la cotisation à l'historique
        self.mois = mois
        self.montant = 10000
        dat_hist = f"{self.nom} {self.separation} {self.montant}"

        if mois not in self.historique_cotisations:
            self.historique_cotisations[mois] = []
        self.historique_cotisations[mois].append(dat_hist)

    def mois_existe_cotisation(self, mois):
        i=0
        for ex_mois in self.historique_cotisations:
            if mois.strip() == ex_mois:
                i += 1
                break
        #print(i)
        return True if i > 0 else False
                

    def total_cotiser(self): #retourne la somme totale cotisée
        total , e = 0, ""
        for elem, liste in self.historique_cotisations.items():
            if liste:
                for ligne in liste:
                    e = str(ligne).split(self.separation)[1].strip()
                    total += int(e)
        return total



class MembreVIP(Membre):
    def __init__(self, nom, telephone, plafond_pret=0):
        super().__init__(nom, telephone)
        self.plafond_pret = plafond_pret
        self.prets_en_cours = [] #prets_en_cours


    def demander_pret(self, montant):
        #accepte si montant <= plafond_pret
        if montant <= self.plafond_pret:
            self.prets_en_cours.append(montant)
        else:
            print("pret refusé")

    def cotiser(self, mois):
        self.mois = mois
        self.montant = 25000
        dat_hist = f"{self.nom} {self.separation} {self.montant}"
        if mois not in self.historique_cotisations:
            self.historique_cotisations[mois] = []
        self.historique_cotisations[mois].append(dat_hist)
    

Fotso = Membre("Fotso", "23547878")
Fotso.cotiser("janvier")

Fotso.cotiser("mars")

Nana = MembreVIP("Nana", "4578965", 50000)
Nana.cotiser("janvier")
Fotso.cotiser("janvier")

Nana.demander_pret(30000)
Nana.cotiser("avril")

print(Fotso.historique_cotisations)
print("---------------")
print(Nana.historique_cotisations)
print("---------------")
print(Nana.prets_en_cours)
print("\nTotal cotiser")

print(Fotso.total_cotiser())
print(Nana.total_cotiser())
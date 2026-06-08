
class Client:
    separateur = "|"
    def __init__(self,nom, telephone, solde_creance=0):
        self.nom = nom
        self.telephone = telephone
        self.solde_creance = solde_creance
        self.historique_paiement = {
            "creance" : [],
            "paiement" : [],
            "erreur" : []
        }

    def est_en_retard(self, jours_limite=30):
        #retourne True si créance existe
        #self.jours_limite = jours_limite
        return True if self.solde_creance > 0 else False
    
    def ajouter_creance(self, montant=0, description=""):
        #augmente le solde, ajoute à l'historique
        self.montant = montant
        self.description = description
        #if self.est_en_retard():
        self.solde_creance = self.solde_creance + self.montant
        dat_hist = f"{self.nom} {self.separateur} -{self.montant} {self.separateur} {self.solde_creance} {self.separateur} {self.description}" 
        self.historique_paiement["creance"].append(dat_hist)
        #else:
        #    dat_hist = f"{self.nom} solde creance négatif"# {self.montant} - {self.solde_creance}"
        #    self.historique_paiement["erreur"].append(dat_hist)            
        return self.afficher_historique()

    def payer(self, montant): 
        #réduit le solde, refuse si montant > solde
        self.montant = montant
        if self.solde_creance > montant :            
            self.solde_creance = self.solde_creance - montant
            dat_hist = f"{self.nom} {self.separateur} -{montant} {self.separateur} {self.solde_creance}"
            self.historique_paiement["paiement"].append(dat_hist)
        else:
            dat_hist = f"{self.nom} erreur de paiement {montant} contre {self.solde_creance}"
            self.historique_paiement["erreur"].append(dat_hist)
        return self.afficher_historique()

    def afficher_historique(self):
        # affiche tous les mouvements
        resultat = []
        for type_mouv, liste in self.historique_paiement.items():
            if liste:
        #        print(f"\n {type_mouv.upper()}:")
                for ligne in liste:
                    resultat.append(ligne)
        return resultat
        #print(f"Solde actuel : {self.solde_creance}\n")
        #return self.historique_paiement

    @staticmethod
    def total_creance(dat_hist=[]):
        t_creance = 0
        print("Historique des operations")
        for dict_hist in dat_hist:
            for type_operat, liste in dict_hist.items():                
                if liste:
                    print(f"{type_operat} : {liste}")
                    for elem in liste:                        
                        mont = str(elem.split(" | ")[2]).strip()
                        t_creance += float(mont)
        return t_creance

historique = []
Andre = Client("Andre", "23101545", 3000)
Andre.payer(1000)
Luc = Client("Luc", "23101545", 3400)
Luc.payer(500)
Franck = Client("Franck", "231101545", 8750)
Franck.ajouter_creance(1750, "Achat Vin")
Andre.ajouter_creance(1000)

historique.append(Andre.historique_paiement)
historique.append(Luc.historique_paiement)
historique.append(Franck.historique_paiement)

print(f"Total creances : {Client.total_creance(historique)}")
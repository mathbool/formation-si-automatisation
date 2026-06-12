
class LimitJournaliereError(Exception):
    pass


class CompteBancaire:

    def __init__(self, titulaire, solde_initial = 0):
        self.titulaire = titulaire
        self.__solde = solde_initial
        self.key_comptes, self.key_transactions = "comptes", "transactions"
        self.liste_comptes = {
            self.key_comptes : [],
            self.key_transactions : []
        }
        self.plafond_retrait = 50000
        self.retrait_total = 0
        self.depot, self.retrait = "depot", "retrait"
        self.liste_transactions = {
            self.depot : [],
            self.retrait : []
        }
        self.retraits = {}

    @property
    def solde(self):
        return self.__solde
    
    @solde.setter
    def solde(self):
        raise AttributeError("Utilisez deposer() ou retirer() pour modifier le solde")

    def deposer(self, montant=0):
        if montant > 0:
            self.__solde += montant
        ligne_depot = f"{self.titulaire} | {self.depot} {montant} | {self.__solde}"
        self.liste_comptes[self.key_transactions].append(ligne_depot)

    def retirer(self, montant=0, jour = ""):
        self.montant = montant
        self.jour = jour
        dispo_retrait = self.plafond_retrait - self.retrait_total
        if self.retrait_journalier():
            msg = f"""Retrait de {montant} '{jour}' par {self.titulaire} Impossible. 
            Plafond retrait max du jour {jour} atteint {self.retrait_total + montant} 
            \nmontant disponible : {dispo_retrait}"""
            raise LimitJournaliereError(msg)
        else:
            if montant <= self.__solde:
                self.__solde -= montant
                if jour not in self.retraits:
                    self.retraits[jour] = []
                self.retraits[jour].append(montant)
                ligne_retrait = f"{jour} | {self.titulaire} | {self.retrait} | {montant} | {self.__solde}"
                self.liste_comptes[self.key_transactions].append(ligne_retrait)               
            else:
                print("Impossible d'effectuer l'opération. solde insuffisant !")


    def afficher_solde(self):
        print(f" le solde de {self.titulaire} est de :  {self.__solde}")

    def liste_des_comptes(self):
        return self.liste_comptes.items()

    def retrait_journalier(self):
        self.retrait_total = 0
        for j, m in self.liste_comptes.items():
            if j == self.key_transactions:
                for elem in m:
                    el = str(elem).split(" | ")
                    trans = el[2].strip()
                    jr = el[0].strip()
                    if jr == self.jour:
                        n = int(str(elem).split(" | ")[3].strip()) if trans == self.retrait else 0
                        self.retrait_total += n
        return self.retrait_total + self.montant >= self.plafond_retrait or self.montant > self.plafond_retrait


Fotso = CompteBancaire("Fotso", 200000)
try:
    Fotso.retirer(30000, "mardi")
    Fotso.retirer(30000, "mercredi")
    Fotso.retirer(30000, "mardi")
except LimitJournaliereError as e:
    print(e)
    
Obam = CompteBancaire("Obam", 45000)
Obam.retirer(2000, "mardi")

#Fotso.afficher_solde()

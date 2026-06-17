
from exceptions import PaiementInsuffisantError

class Caisse:

    def __init__(self):
        self.historique_caisse = []
        self.__solde_caisse = 0

    def paiement(self, montant_commande, montant_encaisser):
        self.montant_commande = montant_commande
        self.montant_encaisser = montant_encaisser
        try:
            reponse = self.encaisser()
            self.historique_caisse.append(reponse)
        except PaiementInsuffisantError as e:
            self.historique_caisse.append(e)

    @property
    def solde(self):
        return self.__solde_caisse()
    
    @solde.setter
    def solde(self):
        return AttributeError("Veuillez effectuer un paiement pourmodifier le solde")
    
    def encaisser(self):
        erreur = ""
        
        if self.montant_encaisser < self.montant_commande:
            erreur = "Montant insuffisant pour paiement"
            raise PaiementInsuffisantError(erreur)
        else:
            r = self.rembourser()
            erreur = f"Encaisser: {self.montant_encaisser} et rembourser: {r}"
            #self.historique_caisse.append(erreur)
        return erreur

    def rembourser(self):
        
        return self.montant_encaisser - self.montant_commande
        
        #self.historique_caisse.append
from .produits import Produit, Plat, Boisson, Dessert
from .exceptions import CommandeVideError, StockEpuiseError

class Commande:
    liste_commande = []
    nb_commandes = 0
    
    def __init__(self, produits):
        self.produits = produits
        self.total_HT, self.total_TTC, self.tva = 0, 0, 0
        #self.liste_commande = []

    def enregistrer_commande(self, code_produit, quantite = 1):
        #trouve = False
        for d in self.produits:
            for cle, elem in d.items():
                if elem == code_produit:
                    
                    if d['stock'] >= quantite:                       
                        #d['quantite'] += quantite
                        if 'quantite' in d:
                            d['quantite'] += quantite 
                        else:
                            d['quantite'] = quantite  

                        d['stock'] -= d['quantite']
                        d['montant'] = d['prix'] * quantite
                        self.nb_commandes += 1

                        Commande.liste_commande.append(d)
                        return True
                    else:
                        raise StockEpuiseError(f"Stock {d['code']} insuffisant : max {d['stock']}")
                    #break

    def calcul_commande(self, liste_commande):
        Commande.liste_commande = liste_commande
        for d in Commande.liste_commande:
            self.total_HT += d["prix"] * d["quantite"]
            self.tva += self.total_HT * d["tva"]
        self.total_TTC += self.total_HT + self.tva

        return {
            'total ht': self.total_HT,
            'tva' : self.tva, 
            'total ttc' : self.total_TTC
        }
        
    def afficher_commande(self):
        print("Commande effectuée")
        print(Commande.liste_commande)
        if Commande.liste_commande:
            print("Produit(s) commandé(s)")
            return Commande.liste_commande    
        else:
            raise CommandeVideError("Commande vide, veuillez commander au moins un produit")
    

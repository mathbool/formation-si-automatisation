
class Produit :
    i=0
    def __init__(self, nom, categorie, prix, stock):
        self.nom =nom
        self.categorie = categorie
        self.prix = prix
        self.stock = stock
        self.seuil_alerte = 10
        self.i= self.i+1

    def afficher(self):
        print(f"{self.i}- {self.nom} | {self.categorie} | {self.prix}" )

    def vendre(self, quantite):
        self.reste = self.stock-quantite
        print(f"quantité vendue {quantite}, montant :{quantite*self.prix} \n stock restant {self.reste}")
        self.alerte_stock()

    def est_disponible(self):
        return True if self.reste > 0 else False
    
    def alerte_stock(self):
        if self.reste < self.seuil_alerte:
            return print("Le stock est épuisé")

biere = Produit("33 Export", "Bière", 800, 48)
biere.afficher()
biere.vendre(50)
print(biere.est_disponible())


'''biere = Produit("Booster", "Bière", 700, 25)
biere.afficher()
biere.vendre(18)
print(biere.est_disponible())'''
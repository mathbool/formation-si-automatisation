
class Produit:
    liste_produits = []
    def __init__(self, code, categorie, description, prix, stock_initial):
        self.code = code 
        self.categorie = categorie
        self.description = description
        self.prix = prix
        self.stock = stock_initial
        #self.categorie_produit = ""
        self.ligne_produit = dict()        
    
    def enregistrer_produit(self):        
        if len(Produit.liste_produits) > 0:
            for elem in Produit.liste_produits:
                if elem["code"] == self.code:
                    print(f"Doublon détecté veuillez modifier le code du produit '{elem['code']}'")
                    print("----------")
                    return             
        self.ligne_produit = {
            "code" : self.code,
            "categorie" : self.categorie,
            "categorie_produit" : self.categorie_produit,
            "description" : self.description,
            "prix" : self.prix,
            "stock" : self.stock,
            "tva" : self.tva
        }        
        Produit.liste_produits.append(self.ligne_produit)
        #print(self.liste_produits)

    def afficher_produit(self):
        return Produit.liste_produits

class Boisson(Produit):
    
    def __init__(self, code, categorie, description, prix, stock_initial, tva):
        self.categorie_produit = "boissons"
        self.tva = tva
        super().__init__(code, categorie, description, prix, stock_initial)
    
    
class Plat(Produit):
    def __init__(self, code, categorie, description, prix, stock_initial, tva):
        self.categorie_produit = "plats"
        self.tva = tva
        super().__init__(code, categorie, description, prix, stock_initial)

    
class Dessert(Produit):
    def __init__(self, code, categorie, description, prix, stock_initial, tva):
        self.categorie_produit = "desserts"
        self.tva = tva
        super().__init__(code, categorie, description, prix, stock_initial)

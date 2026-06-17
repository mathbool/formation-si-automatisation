
from leqg_system.produits import Produit, Boisson, Plat, Dessert
from leqg_system.commandes import Commande
from leqg_system.personnel import Personnel, Serveur, Barman
from leqg_system.rapport import Rapport


p1 = Boisson("b01","biere", "33 export", 300, 10, 0.1925)
p2 = Boisson("b02","biere", "Kadji", 400, 10, 0.1725)
p3 = Plat("p01","diner", "ndole", 500, 10, 0.1825)

p1.enregistrer_produit()
p2.enregistrer_produit()
p3.enregistrer_produit()

p = p3.liste_produits

c = Commande(p)
c1 = c.enregistrer_commande("b01",2)
c2 = c.enregistrer_commande("b02",2)
c3 = c.enregistrer_commande("b01",2)
c4 = c.enregistrer_commande("p01",1)
c5 = c.enregistrer_commande("p01",3)

print(c.afficher_commande())

print("Calcul de la commande !!!!!!!!!")
print(c.calcul_commande(c.liste_commande))


s = Serveur("Henri",150)
print(f"commission de {s.nom} : {s.calacul_commission()}")

r = Rapport(c.liste_commande)
print(r.afficher_rapport())
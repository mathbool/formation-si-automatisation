from validateurs import Validateur
import exceptions
from rapport import Rapport

v = Validateur()
p1 = {"code_produit" : "ART-123A", "prix": 250, "quantite" : 2}
p2 = {"code_produit" : "ART-223A", "prix": 250, "quantite" : 0}
p3 = {"code_produit" : "ART-323A", "prix": -52, "quantite" : 2}
p4 = {"code_produit" : "ART-423A", "prix": 250, "quantite" : 2}
p5 = {"code_produit" : "ART-523hA", "prix": 250, "quantite" : 2}

v.valider_ligne(p1)
v.valider_ligne(p2)
v.valider_ligne(p3)
v.valider_ligne(p4)
v.valider_ligne(p5)

l = v.valider_fichier()

r = Rapport(l)

r.rapport()
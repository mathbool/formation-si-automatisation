from lecteur import LecteurDonnees
from transformateur import Transformateur
from generateur import GenerateurRapport

p1 = {"code_produit" : "ART-123A", "prix": 250, "quantite" : 2, "montant" : 500}
p2 = {"code_produit" : "ART-223A", "prix": 300, "quantite" : 3, "montant" : 600}
p3 = {"code_produit" : "ART-323A", "prix": 400, "quantite" : 2, "montant" : 800}
p4 = {"code_produit" : "ART-423A", "prix": 500, "quantite" : 2, "montant" : 1000}
p5 = {"code_produit" : "ART-523hA", "prix": 600, "quantite" : 2, "montant" : 1200}

d = [p1, p2, p3, p4, p5]

l = LecteurDonnees()
d = l.charger(d)

t = Transformateur()
r = t.calculer_kpi(d)

g = GenerateurRapport()
g.generer(r,"Rapport formaté de vente")
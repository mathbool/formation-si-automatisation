
class Rapport:

    def __init__(self, donnees_commande):
        self.donnees_commande = donnees_commande

    def afficher_rapport(self):
        ca_jour, minim, maxim, nb_commande = 0, 0, 0, 0
        min_prod, max_prod, ca_prod = "", "", ""
        for c in self.donnees_commande:
            ca_jour += c['montant']            
            nb_commande += c['quantite']
            if minim == 0:
                minim = c['montant']
                min_prod = c['code'] + " " + c['description'] 
            if c['montant'] < minim:
                minim = c['montant']
                min_prod = c['code'] + " " + c['description']
            if c['montant'] > maxim:
                maxim = c['montant']  
                max_prod = c['code'] + " " + c['description']          
        nb_commande = len(self.donnees_commande)

        st = f"""
            ca_journalier {ca_jour}
            produit le plus vendu : {max_prod} - {maxim}
            vente minimale : {min_prod} - {minim}
            vente maximal : {max_prod} - {maxim}
            nombre de commande : {nb_commande}"""
        return st
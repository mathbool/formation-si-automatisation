
class Transformateur:

    def __init__(self):
        self.ca_total, self.moyenne, self.minim, self.maxim = 0, 0, 0, 0

    def calculer_kpi(self, donnees):
        self.donnees = donnees
        for dat in donnees:
            if dat:
                for cle, elem in dat.items():
                    if cle == 'montant':
                        if self.minim ==0:
                            self.minim = elem
                        self.ca_total += elem
                        if elem < self.minim:
                            self.minim = elem
                        if elem > self.maxim:
                            self.maxim = elem

        return {
            "Chiffre d'affaires" : self.ca_total, 
            "Moyenne" : self.ca_total / len(donnees), 
            "Minimum" : self.minim, 
            "Maximum" : self.maxim
        }
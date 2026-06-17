
class Personnel:

    def __init__(self, nom, poste):
        self.poste = poste
        self.nom = nom
        self.commission = 0

    def calacul_commission(self):
        self.commission = self.commission

class Serveur(Personnel):

    def __init__(self, nom, prime = 0):        
        self.poste = "Serveur"
        self.prime = prime
        super().__init__(nom, self.poste)

    def calacul_commission(self):
        self.commission = self.prime
        return self.commission

class Barman(Personnel):

    def __init__(self, nom, montant = 0):
        self.montant = montant
        self.poste = "Barman"
        super().__init__(nom, self.poste)
        
    
    def calacul_commission(self):        
        pourcentage = 0.02
        self.commission = self.montant * pourcentage
        return self.commission
        
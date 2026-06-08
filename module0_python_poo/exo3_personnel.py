
class Employe:

    def __init__(self, nom, salaire_base, poste):
        self.nom = nom
        self.salaire_base = salaire_base
        self.poste = poste
        self.prime_fixe = 0

    def calculer_salaire(self):        
        return self.salaire_base

    def se_presenter(self):
        print(f"Employé : {self.nom}\nPoste : {self.poste}")
        print(f"Salaire de base : {self.salaire_base}")
        print(f"Prime fixe: {self.prime_fixe}")
        print(f"Salaire : {self.calculer_salaire()}")

class Enseignants(Employe):

    def __init__(self, nom, salaire_base, heure_cours, taux_horaire):
        super().__init__(nom, salaire_base, "Enseignant")
        self.heure_cours = heure_cours
        self.taux_horaire = taux_horaire
        self.prime_fixe = self.heure_cours * self.taux_horaire

    def calculer_salaire(self):
        return self.salaire_base + self.prime_fixe 
        
class AdminSchool(Employe):

    def __init__(self, nom, salaire_base, prime_fixe):
        super().__init__(nom, salaire_base, "admins")
        self.prime_fixe = prime_fixe

    def calculer_salaire(self):
        return self.salaire_base + self.prime_fixe

equipe = [
    Enseignants("Tamo", 20000, 12, 2000),
    Enseignants("Marie", 18000, 8, 1500),
    AdminSchool("Paul", 25000, 5000),
    AdminSchool("Jeanne", 22000, 3000),
]

for employe in equipe:
    employe.se_presenter()
    print("---")

# Masse salariale totale
total = sum([e.calculer_salaire() for e in equipe])
print(f"\nMasse salariale totale : {total} XAF")
#Tamo = Enseignants("Tamo", 20000, 12, 2000)
#Tamo.se_presenter()
class Voiture:
    def __init__(self, marque, modele, annee, couleur):
       self.marque = marque
       self.modele = modele
       self.annee = annee
       self.couleur = couleur
    def __str__(self):
        return f"{self.marque},{self.modele},({self.annee})-{self.couleur}"

voiture1 = Voiture("Renault", "Clio", 2018, "rouge")
print(voiture1)

class CompteBancaire:
   def __init__(self, titulaire, solde=0):
       self.titulaire = titulaire
       self.solde = solde
   def depose(self, argent):
    self.solde += argent
   def retire(self, argent):
     if self.solde >= argent:
       self.solde -= argent
     else:
       print("Fonds insuffisants")
   def __str__(self):
    return f"Titulaire : {self.titulaire}, Solde : {self.solde:.2f} €"
compte1 = CompteBancaire("Alice", 1000)
compte1.depose(200)
compte1.retire(500)
print(compte1) # Affiche : Titulaire : Alice, Solde : 700.00 €

#Rectangle #3
class Rectangle:
    def __init__(self, longueur, largeur):
      self.longueur = longueur
      self.largeur = largeur
    def aire(self):
      return self.longueur * self.largeur
    def perimetre(self):
      return 2 * (self.longueur + self.largeur)
rectangle1 = Rectangle(4, 3)
print(f"Aire: {rectangle1.aire()}") # Affiche : Aire: 12
print(f"Périmètre: {rectangle1.perimetre()}") # Affiche : Périmètre: 14

#Exo4
import math
class Cercle:
 def __init__(self, rayon):
   self.rayon = rayon
 def aire(self):
  return math.pi * (self.rayon ** 2)
 def perimetre(self):
  return 2 * math.pi * self.rayon
cercle1 = Cercle(5)
print(f"Aire: {cercle1.aire():.2f}") # Affiche : Aire: 78.54
print(f"Périmètre: {cercle1.perimetre():.2f}") # Affiche : Périmètre: 31.42

#Exo5
class Etudiant:
 def __init__(self, nom, prenom, age):
   self.nom = nom
   self.prenom = prenom
   self.age = age
   self.notes = []
 def ajoute_note(self, note):
  self.notes.append(note)
 def moyenne(self):
   return sum(self.notes) / len(self.notes)
etudiant1 = Etudiant("Dupont", "Jean", 21)
etudiant1.ajoute_note(14)
etudiant1.ajoute_note(16)
etudiant1.ajoute_note(12)
print(f"Moyenne: {etudiant1.moyenne()}") # Affiche : Moyenne: 14.0



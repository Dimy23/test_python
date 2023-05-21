"""
Créez une classe Animal avec les attributs et méthodes suivantes :
nom : str
age : int
str() : retourne les informations de l'animal
Créez ensuite deux classes héritées de Animal :
Chien, avec une méthode aboie() qui affiche "Wouaf !"
Chat, avec une méthode miaule() qui affiche "Miaou !"
"""
class Animal:
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"{self.nom},{self.age}"
class Chien(Animal):
    def aboie(self):

     print("Wouaf")
class Chat(Animal):
   def miaule(self):
     print("miaou")

chien1 = Chien("Boule",3)
chien1.aboie()
print(chien1)
chat1 = Chat("Gault",2)
chat1.miaule()
print(chat1)

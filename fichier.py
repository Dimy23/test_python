texte = input("Ecrivez le texte que vous voulez dans le fichier")
with open("Mon_fichier.txt",'a') as f:
    f.write("\n"+texte)

with open("Mon_fichier.txt",'r') as f:
    contenu = f.read()
    print(contenu)

with open("Mon_fichier.txt",'r') as f:
    for ligne in f:
        print(ligne.strip())

import csv
donnees = [
 ["Nom", "Prénom", "Âge"],
 ["Dupont", "Jean", 28],
 ["Durand", "Marie", 42],
 ["Martin", "Luc", 36]
]
with open("mon_fichier.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for ligne in donnees:
        writer.writerow(ligne)

        import csv

        with open("mon_fichier.csv", "r") as f:
            reader = csv.reader(f)
            for ligne in reader:
                print(ligne)




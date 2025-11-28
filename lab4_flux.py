

seuil = 10  # note minimale pour être admis 

try:
    note = float(input("Entrez la note de l'étudiant : "))
except ValueError:
    print("Saisie invalide : veuillez entrer un nombre.")
    exit(1)

if note < 0 or note > 20:
    print("Note hors plage. Elle doit être comprise entre 0 et 20.")
    exit(1)

# Décision
if note >= seuil:
    print("Admis")

    if note >= 16:
        print("Mention : Très bien")
    elif note >= 14:
        print("Mention : Bien")
    elif note >= 12:
        print("Mention : Assez bien")
else:
    
    if  note < seuil:
        print("Rattrapage")
    else:
        print("Refusé")

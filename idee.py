def saisir_notes():
    seuil = 10
    notes = []
    max_notes = 10
    compteur = 0

    print("Entrez des notes. Tapez 'stop' pour terminer.")
    while compteur < max_notes:
        entree = input(f"Note {compteur+1}/{max_notes} : ").strip()

        if entree.lower() == "stop":
            print("Saisie arrêtée par l'utilisateur.\n")
            break
        try:
            note = float(entree)
            notes.append(note)
            compteur += 1
        except ValueError:
            print("Entrée invalide, veuillez entrer un nombre.")
            continue
    else:
        print("Nombre maximum de notes atteint.\n")

    print("Résultats :")
    for index, note in enumerate(notes, start=1):
        statut = "Admis" if note >= seuil else "Refusé"
        print(f"Étudiant {index}: note {note} → {statut}")

    if notes:
        moyenne = sum(notes) / compteur
        if moyenne >= 15:
              mention = "Très bien"
        elif moyenne >= 12:
               mention = "Assez bien"  
                  
        elif moyenne >= 10:
             mention = "passable"       
    


mot_cle = "stop"
message = "" 

while message.lower() != mot_cle:
    message = input("Tapez un message (ou 'stop' pour quitter) : ")

    if message.lower() != mot_cle:
        if message.strip() == "":
            print("Vous avez entré une chaîne vide.")
        else:
            print(f"Vous avez saisi : {message}")

print("Boucle terminée, mot-clé détecté.")


  
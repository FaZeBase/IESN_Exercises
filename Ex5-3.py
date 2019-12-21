def print_all(contacts: dict) -> None :
    nom, email = contacts["nom"], contacts["email"]
    print("Nom: ",nom, " - Email:",email)
contacts = {'nom': 'lolo', 'email': 'lolo@kel.net'}
print_all(contacts)

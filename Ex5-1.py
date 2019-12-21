def update_contact(contacts: dict, name: str, mail: str) -> None :
    '''
    for search_name in contacts.values():
        print(search_name)
        if search_name == name :
            contacts["email"] = mail
        else :
            contacts["nom"] = name
            contacts["email"] = mail
            print("test")
            '''
    contacts[name] = mail
    print(contacts)
contacts = {"lolo": "lolo@be"}
print(contacts)
update_contact(contacts, "lola", "lolo@kel.net")


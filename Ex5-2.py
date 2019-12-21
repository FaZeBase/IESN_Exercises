def print_mail(contacts: dict, name: str) -> None :
    if name in contacts :
        print(contacts[name])
print_mail({"lolo": "lolo@gmail.net"}, "lolo")

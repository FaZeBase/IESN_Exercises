familles_célèbres = {
    "Simpson" : {
        "nb_membres" : 5, "père" : "Homer", "mère" : "Marge",
        "enfants" : ["Bart", "Elisa", "Maggie"],
        "animaux" : [("chat", "Petit Papa Noël" ), ("chien", "Boule de Neige")]},
    "Groseille" : {
        "nb_membres" : 7, "père" : "Fredo", "mère" : "Marcelle",
        "enfants" : ["Franck", "Roselyne", "Million", "Toc-Toc", "Ghislaine"],
        "animaux" : []},
    "Addams" : {
        "nb_membres" : 4, "père" : "Gomez", "mère" : "Morticia",
        "enfants" : ["Mercredi", "Pugsley Uno"],
        "animaux" : [("main", "La Chose")]}
}



for family in familles_célèbres: # print Simpson puis Groseille puis Addams
    print(familles_célèbres[family]["enfants"][-1])
    
print(len(familles_célèbres["Simpson"]["animaux"])) # Attention ! Un tuple a les charactéristiques et le nom de chaque animal

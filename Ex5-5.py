def sort_keys(d :dict) -> tuple :
    keypairs = d.items()
    strings = {}
    ints = {}
    for k,v in keypairs :
        if type(k) == str :
            strings[k] = v
        elif type(k) == int :
            ints[k] = v
        else :
            print("Nope")
    print(ints, strings)
sort_keys({"keyd": 0, "no": 1, 11:69,44:48})

        

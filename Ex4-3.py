
def replace_non_zero(lst: list) -> None :
    i = 0
    while i < len(lst) :
        if lst[i] != 0 :
            lst[i] = 1
        i += 1
    print(lst)
replace_non_zero([1,5,4,7,0,4,0])

def replace_non_zero_alt(lst) :
    for i in lst :
        print(1)
        lst[i] = 1

replace_non_zero_alt([1,5,4,7,0,4,0])

def swap_min_first(lst: list) -> None :
    lst = [69,420,666]
    i = lst.index(min(lst)) + 1
    lst.insert(0, min(lst))
    del lst[i]
    lst.insert(i, lst[1])
    del lst[1]
    print(lst)

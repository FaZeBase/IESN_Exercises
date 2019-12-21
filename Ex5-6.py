def common_pairs(d1: dict, d2: dict) -> list:
    item_d1 = d1.items()
    item_d2 = d2.items()
    val_equals = []
    for i in item_d1:
        if i in item_d2 :
            val_equals.append(item_d1)
    return val_equals
d1 = {"test": 1, "test2": 2, "test3": 3}
d2 = {"test2": 2, "test3": 3}
print(common_pairs(d1 ,d2))

def prime(nb_a_analyser) :
    divisible = 1
    multiplicateur = 1
    while multiplicateur <= 10 and divisible < multiplicateur :
        divisible = nb_a_analyser % multiplicateur
        print(divisible)
        multiplicateur += 1
    if divisible :
        return True
    else :
        return False
print(prime(5))

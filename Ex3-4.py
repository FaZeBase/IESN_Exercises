def ip(ip1,ip2,ip3,ip4) :
    if 0 < ip1 <= 255 and 0 < ip2 <= 255 and 0 < ip3 <=255 and 0 < ip4 <= 255 :
        print(ip1,ip2,ip3,ip4,sep='.')
    else :
        print("L'un des nombres est invalide")

ip(1,2,3,4)


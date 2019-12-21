def ip_verify(ip) :
    if 0 < ip <= 255 :
        return True
    else :
        return False
def ip(ip1,ip2,ip3,ip4) :
    ip_valid = ip_verify(ip1) and\
               ip_verify(ip2) and\
               ip_verify(ip3) and\
               ip_verify(ip4)
    if ip_valid :
        print(ip1,ip2,ip3,ip4,sep='.')
    else :
        print("Il y a un problème avec cette addresse IP !")

ip(1,2,3,4)


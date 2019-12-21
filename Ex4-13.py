def antipode(coord : tuple) -> None :
    coord1 = coord[0]
    coord2 = coord[1]
    if -90 < coord1 < 90 and -180 < coord2 < 180 :
        coord1 = -coord1
        if coord2 <= 0 :
            coord2 += 180
        else :
            coord2 -= 180
        print(coord1,coord2)
    else :
        print("Vérifiez vos coordonées")
coord = (45.147929, 26.803969)
antipode(coord)

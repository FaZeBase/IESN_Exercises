def bissextile(year) :
    if year %4 == 0 and not year % 400 == 0 or year % 100 == 0 :
        return "oui"
    else :
        return "non"
def days_in_month(month,bissextile) :
    
    if month == "janvier" :
        return 31
    elif month == "février" :
        if bissextile == "oui" :
            return 29
        else :
            return 28
    elif month == "mars" :
        return 31
    elif month == "avril" :
        return 30
    elif month == "mai" :
        return 31
    elif month == "juin" :
        return 30
    elif month == "juillet" :
        return 31
    elif month == "août" :
        return 31
    elif month == "septembre" :
        return 31
    elif month == "octobre" :
        return 30
    elif month == "novembre" :
        return 31
    elif month == "décembre" :
        return 31
    else :
        return False
bissextile_check = bissextile(2019)
print(days_in_month("février",bissextile_check))

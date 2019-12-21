def str_to_low(s: str) -> str :
    string = ""
    for i in s :
        temp = ord(i)
        if 'A' <= i <= 'Z' :
            temp += 32
        temp = chr(temp)
        string += temp
    return string
print(str_to_low("XYZ"))


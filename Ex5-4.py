def letters_count(word: str) -> dict :
    dic = {}
    for letter in word :
        if letter in dic :
            dic[letter] += 1
        else :
            dic[letter] = 1
    print(dic)
letters_count("tester")

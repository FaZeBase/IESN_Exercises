def count_chars(chars: str, s: str) -> int :
    counter = 0
    for char in chars :
        for string in s :
            if chars[chars.index(char)] == s[s.index(string)] :
                counter += 1
    return counter
print(count_chars("abc", "aabbbccddd")) 

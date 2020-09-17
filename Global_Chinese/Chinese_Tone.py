conso = [
    ["a", "ā", "á", "ǎ", "à"],
    ["o", "ō", "ó", "ǒ", "ò"],
    ["e", "ē", "é", "ě", "è"],
    ["i", "ī", "í", "ǐ", "ì"],
    ["u", "ū", "ú", "ǔ", "ù"],
]


def Tone(word, n):
    word = str(word)
    if "a" in word:
        word = word.replace("a", conso[0][n])
        return word
    elif "o" in word or "e" in word:
        if "o" in word:
            word = word.replace("o", conso[1][n])
            return word
        if "e" in word:
            word = word.replace("e", conso[2][n])
            return word
    elif "i" in word or "u" in word:
        if "i" in word and "u" in word:
            if word.index("i") > word.index("u"):
                word = word.replace("u", conso[4][n])
                return word

            else:
                word = word.replace("i", conso[3][n])
                return word
        elif "i" in word:
            word = word.replace("i", conso[3][n])
            return word
        else:
            word = word.replace("u", conso[4][n])
            return word


print("zhuang(4) --> ", Tone("zhuang", 4))
print("nian(2) -->", Tone("nian", 2))
print("qiong(2) -->", Tone("qiong", 2))
print("zhuo(3) -->", Tone("zhuo", 3))
print("shiquan(2,2) -->", Tone("shi", 2), Tone("quan", 2))
print("liubai(4,3) -->", Tone("liu", 4), Tone("bai", 3))
print("shiquan(1,4) -->", Tone("san", 1), Tone("wan", 4))

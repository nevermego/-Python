def int_func(word):
    return word.capitalize()

word = input('Insert any text - ')
print("int_func:", int_func(word))


# для нескольких слов, разделеннхы пробелом

def int_func_full(words):
    parts = words.split()
    result = ""

    for part in parts:
        result += int_func(part) + " "

    return result

words = input('Insert any text with spaces - ')
print("int_func_full:", int_func_full(words))
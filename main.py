# Conjugates words :D
def conjugate(word, starter):
    if word.endswith("ar"):
        word = word.removesuffix("ar")
        if starter == "tu":
            word = word + "as"
        elif starter == "yo":
            word = word + "o"
        elif starter == "usted" or starter == "el" or starter == "ella":
            word = word + "a"
    elif word.endswith("er") or word.endswith("ir"):
        word = word.removesuffix("er")
        word = word.removesuffix("ir")
        if starter == "tu":
            word = word + "es"
        elif starter == "yo":
            word = word + "o"
        elif starter == "usted" or starter == "el" or starter == "ella":
            word = word + "e"
    return word # Return the new word, or the fallback old word

# print(conjugate("tome", "usted"))
while True:
    _word = input("What word would you like to conjugate: ")
    _pronoun = input("What pronoun should we use: ")
    print(conjugate(_word, _pronoun))

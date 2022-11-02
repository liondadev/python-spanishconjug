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
    return word

print(conjugate("tomar", "usted"))

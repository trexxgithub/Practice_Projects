#Word Wizard
def magic_banner(func):
    def wrapper(text):
        print("\n Welcome to the Word Wizard")
        result = func(text)
        print("Magic has been executed")
        return result
    return wrapper
#generator
def spell_generator(words):
    for word in words:
        yield f"Spell cast using word: {word}"

@magic_banner
def word_wizard(text):
    print("Original Text" , text)
    print("Length " , len(text))
    print("Reversed", text[::-1])
    print("Uppercase" , text.upper())

    #split
    words = text.split()
    print("Words: ", words)
    print("'magic' in text?" , "magic" in text.lower())

    #lambda
    long_words = list(filter(lambda w: len(w) > 4 , words))
    capitalized = list(map(lambda w: w.capitalize(), words))

    print("Long Words: " , long_words)
    print("Capitalized Words" , capitalized)

    #list comprehension

    word_length = {len(w) for w in words}
    print("Word Lengths: ", word_length)

    #set
    unique_words = set(words)
    print("Unique Words: " , unique_words)

    #dictionary
    stats = {
        "total_words": len(words),
        "unique_words": len(unique_words),
        "long_words": long_words,
    }
    print("\n STATS")
    for key,value in stats.items():
        print(f"{key}: {value}")

    #GENERATOR IN ACTION
    print("\n Spell Event")
    for spell in spell_generator(long_words):
        print(spell)

# entry function

if __name__ == '__main__':
    user_text = input("Enter a magical sentence: \n")
    word_wizard(user_text)





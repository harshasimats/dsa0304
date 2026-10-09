# Program to implement a finite-state machine
# for generating plural forms of English nouns

def plural_fsm(word):
    # State 0: Start state
    state = 0

    # Words ending with s, x, z, ch, sh
    if word.endswith(("s", "x", "z", "ch", "sh")):
        state = 1
        return word + "es"

    # Words ending with consonant + y
    elif word.endswith("y") and len(word) > 1 and word[-2] not in "aeiou":
        state = 2
        return word[:-1] + "ies"

    # Default plural rule
    else:
        state = 3
        return word + "s"


# Test words
words = ["cat", "book", "bus", "box", "baby", "dish", "class"]

print("Finite-State Morphological Parser")
print("-" * 45)

for word in words:
    plural = plural_fsm(word)
    print(word, "->", plural)
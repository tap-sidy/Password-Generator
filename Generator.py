"""Voici mon projet : un générateur de mot de passe"""

import random
import string


def generate_password(min_length, number=True, special_characters=True):

    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    print("Voici tout ce que nous vous proposons pour créer votre mot de passe :")
    
    print("")

    print(letters)
    print(digits)
    print(special)

    print("")

    print("voici votre password")
    characters = letters   
    if number:
        characters = characters + digits
    if special_characters:
        characters = characters + special

    password = ""
    for _ in range(min_length):
        password = password + random.choice(characters)

    return password


print(generate_password(15))

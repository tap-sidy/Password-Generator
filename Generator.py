import random
import string


def generate_password(length, use_digits=True, use_special=True, use_uppercase=True):
    # Lettres de base
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


# ===== Interaction avec l'utilisateur =====

length = int(input("Choisissez la longueur du mot de passe (minimum 15) : "))

if length < 15:
    print(" La longueur minimale est 15 caractères.")
    length = 15
    print("➡ Longueur définie automatiquement à 15.")

use_digits = input("Inclure des chiffres ? (o/n) : ").lower() == "o"
use_special = input("Inclure des caractères spéciaux ? (o/n) : ").lower() == "o"
use_uppercase = input("Inclure des majuscules ? (o/n) : ").lower() == "o"

password = generate_password(length, use_digits, use_special, use_uppercase)

print("\n Mot de passe généré :")
print(password)

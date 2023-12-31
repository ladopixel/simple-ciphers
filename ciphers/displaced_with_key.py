# displaced with key (the key cannot repeat the same letter)
# desplazado con llave (la llave no puede repetir la misma letra)

# key correct: ergo
# key incorrect: repeat (repeats the letter e)

#                   normal alphabet
# ┌--------------------------------------------------┐
# a b c d e f g h i j k l m n o p q r s t u v w x y z 

#   key               rest of alphabet
# ┌-----┐┌------------------------------------------┐
# e r g o a b c d f h i j k l m n p q s t u v w x y z

from typing import List

alphabet_list: List = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt_displaced_with_key(text_string: str, one_key: str) -> str:
    text_string: str = text_string.lower()
    text_string_encrypted: str = ''
    new_alphabet_list: List = []
    positions_in_alphabet: List = []

    # I store the key in the new alphabet first.
    # Almaceno primero la clave en el nuevo alfabeto.
    for one_letter in one_key:
        new_alphabet_list.append(one_letter)

    # I complete the alphabet with the letters that are not in the key.
    # Completo el alfabeto con las letras que no están en la clave.
    for one_letter in alphabet_list:
        if not one_letter in new_alphabet_list:
            new_alphabet_list += one_letter

    # I save the text positions based on the initial alphabet.
    # Guardo las posiciones del texto basándome en el alfabeto inicial.
    for one_letter in text_string:
        positions_in_alphabet.append(alphabet_list.index(one_letter)) 

    # I select the text positions based on the new alphabet.
    # Selecciono las posiciones del texto basándome en el nuevo alfabeto.
    for position in positions_in_alphabet:
        text_string_encrypted: str = text_string_encrypted + new_alphabet_list[position]

    return text_string_encrypted


def decrypt_displaced_with_key(text_encrypt: str, one_key: str) -> str:
    text_encrypt: str = text_encrypt.lower()
    text_string_decrypted: str = ''
    new_alphabet_list: List = []
    positions_in_alphabet: List = []
    
    # I store the key in the new alphabet first.
    # Almaceno primero la clave en el nuevo alfabeto.
    for one_letter in one_key:
        new_alphabet_list.append(one_letter)

    # I complete the alphabet with the letters that are not in the key.
    # Completo el alfabeto con las letras que no están en la clave.
    for one_letter in alphabet_list:
        if not one_letter in new_alphabet_list:
            new_alphabet_list += one_letter

    # I save the text positions based on the initial alphabet.
    # Guardo las posiciones del texto basándome en el alfabeto inicial.
    for one_letter in text_encrypt:
        positions_in_alphabet.append(new_alphabet_list.index(one_letter)) 

    # I select the text positions based on the new alphabet.
    # Selecciono las posiciones del texto basándome en el nuevo alfabeto.
    for position in positions_in_alphabet:
        text_string_decrypted: str = text_string_decrypted + alphabet_list[position]

    return text_string_decrypted
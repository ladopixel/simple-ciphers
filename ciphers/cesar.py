# Cesar | Displacement substitution method
# a → d (with 3 positions)
# b → e (with 3 positions)
# c → f (with 3 positions)
# d → g (with 3 positions)
# ... 

from typing import List

alphabet_list: List = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt_cesar(text_string: str, positions: int) -> str:
    text_string: str = text_string.lower()
    final_string: str = ''
    
    for one_letter in text_string:
        if one_letter != ' ':
            actual_position: int = alphabet_list.index(one_letter)
            final_string: str = final_string + alphabet_list[actual_position + positions]
        else:
            final_string: str = final_string + ' '

    return final_string


def decrypt_cesar(text_string: str, positions: int) -> str:
    text_string: str = text_string.lower()
    final_string: str = ''
    
    for one_letter in text_string:
        if one_letter != ' ':
            actual_position: int = alphabet_list.index(one_letter)
            final_string: str = final_string + alphabet_list[actual_position - positions]
        else:
            final_string: str = final_string + ' '

    return final_string
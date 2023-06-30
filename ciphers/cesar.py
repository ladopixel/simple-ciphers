# Cesar | Displacement substitution method
# a → d (with 3 positions)
# b → e (with 3 positions)
# c → f (with 3 positions)
# d → g (with 3 positions)
# ... 

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt_cesar(text_string, positions):
    text_string = text_string.lower()
    final_string = ''
    
    for one_letter in text_string:
        if one_letter != ' ':
            actual_position = alphabet_list.index(one_letter)
            final_string += alphabet_list[actual_position + positions]
        else:
            final_string += ' '

    return final_string


def decrypt_cesar(text_string, positions):
    text_string = text_string.lower()
    final_string = ''
    
    for one_letter in text_string:
        if one_letter != ' ':
            actual_position = alphabet_list.index(one_letter)
            final_string += alphabet_list[actual_position - positions]
        else:
            final_string += ' '

    return final_string
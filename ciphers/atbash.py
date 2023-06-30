# Atbash | Substitution method
# a → z
# b → y
# c → x
# d → w
# ...
# x → c
# y → b
# z → a

alphabet_list = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

reverse_alphabet_list = [' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m',
                            'l','k','j','i','h','g','f','e','d','c','b','a']


def encrypt_atbash(text_string):
    text_string = text_string.lower()
    reverse_string = ''

    for one_letter in text_string:
        position = alphabet_list.index(one_letter)
        reverse_string += reverse_alphabet_list[position]

    return reverse_string


def decrypt_atbash(text_string_encrypted):
    text_string_encrypted = text_string_encrypted.lower()
    decrypted_string = ''
    
    for one_letter in text_string_encrypted:
        position = reverse_alphabet_list.index(one_letter)
        decrypted_string += alphabet_list[position]

    return decrypted_string
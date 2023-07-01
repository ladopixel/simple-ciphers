# Polibio square

# ┌───┬─────┬─────┬─────┬─────┬─────┐
# │   │  1  │  2  │  3  │  4  │  5  │
# ├───┼─────┼─────┼─────┼─────┼─────┤
# │ 1 │  a  │  b  │  c  │  d  │  e  │
# ├───┼─────┼─────┼─────┼─────┼─────┤
# │ 2 │  f  │  g  │  h  │ ij  │  k  │
# ├───┼─────┼─────┼─────┼─────┼─────┤
# │ 3 │  l  │  m  │  n  │  o  │  p  │
# ├───┼─────┼─────┼─────┼─────┼─────┤
# │ 4 │  q  │  r  │  w  │  t  │  u  │
# ├───┼─────┼─────┼─────┼─────┼─────┤
# │ 5 │  v  │  w  │  x  │  y  │  z  │
# └───┴─────┴─────┴─────┴─────┴─────┘

# Letter a → 11
# Letter w → 52
# Letter i → 24
# Letter j → 24


alphabet_list = [
    ('a', 11), ('b', 12), ('c', 13), ('d', 14), ('e', 15),
    ('f', 21), ('g', 22), ('h', 23), ('i', 24), ('j', 24), ('k', 25),
    ('l', 31), ('m', 32), ('n', 33), ('o', 34), ('p', 35),
    ('q', 41), ('r', 42), ('s', 43), ('t', 44), ('u', 45),
    ('v', 51), ('w', 52), ('x', 53), ('y', 54), ('z', 55)
    ]


def encrypt_polibio_square(text_string):
    text_encrypted = ''
    for one_letter in text_string:
        for letter_alphabet_list in alphabet_list:
                if one_letter == letter_alphabet_list[0]:
                    text_encrypted += str(f'{letter_alphabet_list[1]} ')

    return text_encrypted


def decrypt_polibio_square(text_numbers):
    text_decrypted = ''
    letter_number_list = text_numbers.split(' ')

    for one_letter_number in letter_number_list:
        for letter_alphabet_list in alphabet_list:
             if one_letter_number == str(letter_alphabet_list[1]):
                text_decrypted += str(letter_alphabet_list[0])
     
    return text_decrypted

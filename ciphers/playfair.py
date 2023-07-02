# Playfair

# Removed letter w
# Eliminadas letra w

# key = ergo

# ┌─────┬─────┬─────┬─────┬─────┐
# │  e  │  r  │  g  │  o  │  a  │
# ├─────┼─────┼─────┼─────┼─────┤
# │  b  │  c  │  d  │  f  │  h  │
# ├─────┼─────┼─────┼─────┼─────┤
# │  i  │  j  │  k  │  l  │  m  │
# ├─────┼─────┼─────┼─────┼─────┤
# │  n  │  p  │  q  │  r  │  s  │
# ├─────┼─────┼─────┼─────┼─────┤
# │  t  │  u  │  x  │  y  │  z  │
# └─────┴─────┴─────┴─────┴─────┘

from typing import List

def encrypt_playfair(text_string: str):
    if len(text_string) % 2 != 0: 
        text_string += 'W'

    text_string_two_letters: List = [text_string[i:i+2] for i in range(0, len(text_string), 2)]

    print(text_string_two_letters)


encrypt_playfair('aafqerfasdbnsfhsywertqer')
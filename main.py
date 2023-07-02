from ciphers.atbash import encrypt_atbash, decrypt_atbash
from ciphers.cesar import encrypt_cesar, decrypt_cesar
from ciphers.displaced_with_key import encrypt_displaced_with_key, decrypt_displaced_with_key
from ciphers.polybius_square import encrypt_polybius_square, decrypt_polybius_square


# atbash(string)
# print(encrypt_atbash('hola mundo'))
# print(decrypt_atbash('sloz nfmwl'))


# cesar(string, n positions)
# print(encrypt_cesar('hola mundo', 3))
# print(decrypt_cesar('krod pxqgr', 3))


# encrypt_displaced_with_key(string, key)
# encrypted_word = encrypt_displaced_with_key('holamundo', 'ergo')
# print(encrypted_word)

# decrypt_displaced_with_key(string, key)
# decrypted_word = decrypt_displaced_with_key('dmjekulom', 'ergo')
# print(decrypted_word)


# print(encrypt_polybius_square('wikipediaenciclopedialibre'))
# print('---------')
# print(decrypt_polybius_square('52 24 25 24 35 15 14 24 11 15 33 13 24 13 31 34 35 15 14 24 11 31 24 12 42 15'))
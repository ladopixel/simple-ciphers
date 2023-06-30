from ciphers.atbash import encrypt_atbash, decrypt_atbash
from ciphers.cesar import encrypt_cesar, decrypt_cesar
from ciphers.displaced_with_key import encrypt_displaced_with_key, decrypt_displaced_with_key


# atbash(string)
# print(encrypt_atbash('hola mundo'))
# print(decrypt_atbash('sloz nfmwl'))


# cesar(string, n positions)
# print(encrypt_cesar('hola mundo', 3))
# print(decrypt_cesar('krod pxqgr', 3))


# encrypt_displaced_with_key(string, key)
encrypted_word = encrypt_displaced_with_key('holamundo', 'ergo')
for letter in encrypted_word:
    print(letter)

print('---------')

# decrypt_displaced_with_key(string, key)
decrypted_word = decrypt_displaced_with_key('dmjekulom', 'ergo')
for letter in decrypted_word:
    print(letter)
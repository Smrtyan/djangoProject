from django.test import TestCase

# Create your tests here.

import base64
import hashlib

from Cryptodome.Cipher import AES  # from pycryptodomex v-3.10.4
from Cryptodome.Random import get_random_bytes

HASH_NAME = "SHA512"
IV_LENGTH = 12
ITERATION_COUNT = 65535
KEY_LENGTH = 32
SALT_LENGTH = 16
TAG_LENGTH = 16


def encrypt(password, plain_message):
    salt = get_random_bytes(SALT_LENGTH)
    print("salt")
    print(salt)
    salt = b'\xf2Qd\xdeW#i\xd97i\xbd\x1c\x87\xd8n2'
    iv = get_random_bytes(IV_LENGTH)
    print("iv")
    print(iv)

    secret = get_secret_key(password, salt)
    print("secret")
    print(secret)

    cipher = AES.new(secret, AES.MODE_GCM, iv)

    encrypted_message_byte, tag = cipher.encrypt_and_digest(
        plain_message.encode("utf-8")
    )
    cipher_byte = salt + iv + encrypted_message_byte + tag
    print("tag")
    print(base64.b64encode(tag))
    print(bytes.decode(base64.b64encode(tag)))
    encoded_cipher_byte = base64.b64encode(cipher_byte)
    return bytes.decode(encoded_cipher_byte)


def decrypt(password, cipher_message):
    decoded_cipher_byte = base64.b64decode(cipher_message)

    salt = decoded_cipher_byte[:SALT_LENGTH]
    iv = decoded_cipher_byte[SALT_LENGTH : (SALT_LENGTH + IV_LENGTH)]
    encrypted_message_byte = decoded_cipher_byte[
        (IV_LENGTH + SALT_LENGTH) : -TAG_LENGTH
    ]
    tag = decoded_cipher_byte[-TAG_LENGTH:]
    secret = get_secret_key(password, salt)
    cipher = AES.new(secret, AES.MODE_GCM, iv)

    decrypted_message_byte = cipher.decrypt_and_verify(encrypted_message_byte, tag)
    return decrypted_message_byte.decode("utf-8")


def get_secret_key(password, salt):
    return hashlib.pbkdf2_hmac(
        HASH_NAME, password.encode(), salt, ITERATION_COUNT, KEY_LENGTH
    )


outputFormat = "{:<25}:{}"
secret_key = "your_secure_keyyour_secure_keyyour_secure_keyyour_secure_keyyour_secure_key"
plain_text = "Your_plain_text"

print("------ AES-GCM Encryption ------")
cipher_text = encrypt(secret_key, plain_text)
print(outputFormat.format("encryption input", plain_text))
print(outputFormat.format("encryption input", SALT_LENGTH  * "S"+IV_LENGTH*"I"))
print(outputFormat.format("encryption output", cipher_text))
print(outputFormat.format("encryption outputbase64", base64.b64decode(cipher_text)))
print(outputFormat.format("encryption output len", len(cipher_text)))

decrypted_text = decrypt(secret_key, cipher_text)

print("\n------ AES-GCM Decryption ------")
print(outputFormat.format("decryption input", cipher_text))
print(outputFormat.format("decryption output", decrypted_text))
print(get_random_bytes(10).decode('latin-1'))

s = "configure the network and firewall"
print(s.replace(" ","-"))
#!/opt/immune/etc/env_bin/python
# -*- coding: utf-8 -*-
import rutil
import base64
import logging as log
from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[0 : -s[-1]]


class Cipher(object):
    def __init__(self, password=None):
        if password:
            self._password = password
        else:
            self._password = rutil.get_enc_key()

    def encrypt(self, raw_message):
        raw = pad(raw_message.encode())
        iv = Random.new().read(AES.block_size)
        cipher_text = AES.new(self._password, AES.MODE_CBC, iv)

        return base64.b64encode(iv + cipher_text.encrypt(raw))

    def decrypt(self, encrypted_message):
        try:
            enc = base64.b64decode(encrypted_message)
            iv = enc[:16]
            cipher_text = AES.new(self._password, AES.MODE_CBC, iv)

            return unpad(cipher_text.decrypt(enc[16:]))
        except Exception:
            log.debug("Cannot decrypt. Encrypted message should not be None.")
            return encrypted_message

    def get_decrypted_value_and_status(self, encrypted_message):
        """
        Returns Decrypted value and success = True for correctly encrypted values
        Else returns passed value and success = False for exception
        """
        try:
            enc = base64.b64decode(encrypted_message)
            iv = enc[:16]
            cipher_text = AES.new(self._password, AES.MODE_CBC, iv)
            return unpad(cipher_text.decrypt(enc[16:])), True
        except Exception:
            log.exception("fail")
            return encrypted_message, False


if __name__ == "__main__":
    text = "Bajooka"
    cipher = Cipher()
    encrypted = cipher.encrypt(text)

    x = ""
    for a in encrypted:
        x = x + "'{}',".format(a)
    log.warning(str(x))
    log.warning(encrypted)

    decrypted = cipher.decrypt(encrypted)
    log.warning(decrypted)

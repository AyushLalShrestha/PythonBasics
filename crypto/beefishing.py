from random import randrange

from Crypto.Cipher import Blowfish
from Crypto import Random


def _gen_padding(file_size, block_size):
    pad_bytes = block_size - (file_size % block_size)
    padding = Random.get_random_bytes(pad_bytes - 1)
    bflag = randrange(block_size - 2, 256 - block_size)
    bflag -= bflag % block_size - pad_bytes
    return padding + chr(bflag)


def _read_padding(buf, block_size):
    return (buf[-1] % block_size) or block_size


def generate_iv(block_size):
    return Random.get_random_bytes(block_size)


def get_cipher(key, iv):
    return Blowfish.new(key, Blowfish.MODE_CBC, iv)


def encrypt(in_buf, out_buf, key, chunk_size=4096):
    iv = generate_iv(Blowfish.block_size)
    cipher = get_cipher(key, iv)
    bytes_read = 0
    wrote_padding = False

    out_buf.write(iv)

    while 1:
        buffer = in_buf.read(chunk_size)
        buffer_len = len(buffer)
        bytes_read += buffer_len
        if buffer:
            if buffer_len < chunk_size:
                buffer += _gen_padding(bytes_read, cipher.block_size)
                wrote_padding = True
            out_buf.write(cipher.encrypt(buffer))
        else:
            if not wrote_padding:
                out_buf.write(cipher.encrypt(_gen_padding(bytes_read, cipher.block_size)))
            break


def decrypt(in_buf, out_buf, key, chunk_size=4096):
    iv = in_buf.read(Blowfish.block_size)

    cipher = get_cipher(key, iv)
    decrypted = ''

    while 1:
        buffer = in_buf.read(chunk_size)
        if buffer:
            decrypted = cipher.decrypt(buffer)
            out_buf.write(decrypted)
        else:
            break

    if decrypted:
        padding = _read_padding(decrypted, cipher.block_size)
        out_buf.seek(-padding, 2)
        out_buf.truncate()


def encrypt_file(in_file, out_file, key, chunk_size=4096):
    with open(in_file, 'rb') as in_fh:
        with open(out_file, 'wb') as out_fh:
            encrypt(in_fh, out_fh, key, chunk_size)


def decrypt_file(in_file, out_file, key, chunk_size=4096):
    with open(in_file, 'rb') as in_fh:
        with open(out_file, 'wb') as out_fh:
            decrypt(in_fh, out_fh, key, chunk_size)

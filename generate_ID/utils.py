import random
import re
import hashlib

short_len = 12
valid_short_id = re.compile("^[a-z0-9]{12}$")


def is_short_id(identifier):
    return bool(valid_short_id.match(identifier))


def truncate_id(identifier):
    trim_to = min(short_len, len(identifier))
    return identifier[:trim_to]


def generate_id(crypto=True):
    while True:
        b = bytes(random.getrandbits(8) for _ in range(32))
        if crypto:
            h = hashlib.sha256(b).hexdigest()
        else:
            h = b.hex()
        truncated_id = truncate_id(h)
        try:
            int(truncated_id)
        except ValueError:
            return h


def generate_random_id():
    return generate_id(crypto=True)


def generate_non_crypto_id():
    return generate_id(crypto=False)

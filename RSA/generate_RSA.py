from loguru import logger
from Crypto import Random
from Crypto.PublicKey import RSA

def create_rsa_key():
    try:
        random_gen = Random.new().read
        rsa = RSA.generate(2048, random_gen)

        private_pem = rsa.exportKey()

        with open('private.pem', 'wb') as f:
            f.write(private_pem)
        public_pem = rsa.publickey().exportKey()

        with open('public.pem', 'wb') as f:
            f.write(public_pem)

        return True

    except Exception as e:
        logger.error(f"An error was encountered while creating the rsa key. Error: {e}")
        return False

if __name__ == '__main__':
    create_rsa_key()
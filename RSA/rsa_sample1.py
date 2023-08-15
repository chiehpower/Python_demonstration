from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import os

# 生成RSA密钥对
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# 获取公钥
public_key = private_key.public_key()

# 将公钥保存到文件
with open("public_key.pem", "wb") as public_key_file:
    public_key_file.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("公钥已保存到 public_key.pem 文件")

# 将私钥保存到文件
with open("private_key.pem", "wb") as private_key_file:
    private_key_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

print("私钥已保存到 private_key.pem 文件")


### ------ Decode
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding

# 从文件中加载私钥
with open("private_key.pem", "rb") as private_key_file:
    private_key_data = private_key_file.read()
    private_key = serialization.load_pem_private_key(private_key_data, password=None)

# 要解密的数据
ciphertext = b"\x0b\x9f\xb3U\xf5\xd0\xb2u\x18c\x8b\xd4u\xa4\xdd\x82\xee9\x0c\x05\x9f\x94"

# 解密数据
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("解密后的数据：", plaintext.decode())
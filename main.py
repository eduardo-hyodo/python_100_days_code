from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

salt = b"IwantoopenfileIwantoopenfileIwantoopenfileIwantoopenfileIwantoopenfile"
password = "Iwanttoopenfile"
key = PBKDF2(password, salt, dkLen=32)

with open("./key.bin", "wb") as key_bin:
    key_bin.write(key)

cipher = AES.new(key, AES.MODE_CBC)
with open("./data.json") as secure_data:
    data = secure_data.read()
    data_bytes = bytes(data, "utf-8")

cipher_data = cipher.encrypt(pad(data_bytes, AES.block_size))
with open("./data.bin", "wb") as data_bin:
    data_bin.write(cipher.iv)
    data_bin.write(cipher_data)

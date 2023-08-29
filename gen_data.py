from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import json


class Data:
    def __init__(self):
        with open("../key.bin", "rb") as key:
            new_key = key.read()

        with open("../data.bin", "rb") as data_bin:
            iv = data_bin.read(16)
            new_data = data_bin.read()
            new_cipher = AES.new(new_key, AES.MODE_CBC, iv=iv)
            self.uncipher_data = unpad(new_cipher.decrypt(new_data), AES.block_size)
            # print(str(uncipher_data, "utf-8"))

    def get(self):
        # return json.loads(str(self.uncipher_data, "utf-8"))
        return json.loads(self.uncipher_data)
        # return self.uncipher_data

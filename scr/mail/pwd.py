import base64
import os
import pickle
import hashlib

import binascii


class Pwd:
    def __init__(self):
        pass

    @staticmethod
    def hash(line):
        return hashlib.md5(line.encode("utf-8")).hexdigest()

    @staticmethod
    def encrypt(pwd, master_pwd):
        _pwd_encode_str = base64.standard_b64encode(
            pwd.encode("utf-8"))
        pwd_encode_str = _pwd_encode_str.decode("utf-8")
        m_hash = Pwd.hash(master_pwd)
        _master_encode_str = base64.standard_b64encode(
            m_hash.encode("utf-8"))
        master_encode_str = _master_encode_str.decode("utf-8")

        sum_pwd_master = pwd_encode_str[::-1] + master_encode_str

        res_encode = base64.standard_b64encode(
            sum_pwd_master.encode("utf-8"))
        return res_encode

    @staticmethod
    def save(user, path, data):
        _data = Pwd.load(path)
        ud = {user: data}
        _data.update(ud)
        with open(path, 'wb') as f:
            pickle.dump(_data, f)

    @staticmethod
    def load(path):
        if os.path.isfile(path):
            with open(path, 'rb') as f:
                return pickle.load(f)


    @staticmethod
    def decrypt(data, master):
        decode_data = base64.standard_b64decode(data).decode(
            "utf-8")
        hash_master = Pwd.hash(master)
        hash_master_encode = base64.standard_b64encode(
            hash_master.encode("utf-8"))
        _pwd = decode_data.split(hash_master_encode.decode("utf-8"))[0]
        pwd = _pwd[::-1]
        try:
            pwd_decode = base64.standard_b64decode(pwd).decode(
                "utf-8")
        except binascii.Error:
            pwd_decode = None
        return pwd_decode


if __name__ == '__main__':
    pth = "../etc/pwd.pkl"
    user = "zaswed@gmail.com"
    user2 = "vrabey@gmail.com"
    p = Pwd()
    code = p.encrypt("fasadN", "vrabey")
    Pwd.save(user2, pth, code)
    # data = Pwd.load(pth)
    #
    # data_user = data["zaswed@gmail.com"]
    #
    # if data:
    #     print(Pwd.decrypt(data_user, "vrabey"))
    # else:
    #     print("not")

import base64
import yaml
import hashlib





# rep = str((input(">>> \n")))

# print(rep ==  base64.standard_b64decode(pwd_encode).decode("utf-8"))

def save_password(path, data):
    with open(path, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)

def load_password(path):
    with open(path, "r") as obj:
        return yaml.load(obj)

def get_hash(line):
    return hashlib.md5(line).hexdigest()





pwd_path = "pwd.yaml"
pwd = b"password"
master = b"master"
mh = hashlib.md5(master)
master_hash = mh.hexdigest()
print(master_hash)

pwd_encode = base64.standard_b64encode(pwd)
master_encode = base64.standard_b64encode(master_hash.encode("utf-8"))
print(pwd_encode)
res = pwd_encode.decode("utf-8") + master_encode.decode("utf-8")
res_encode = base64.standard_b64encode(res.encode("utf-8"))
print(res)
print('\n----------------результат --------------- ')
print(res_encode)


print("\nрасшифровка:")

decode_1 =base64.standard_b64decode(res_encode)
print("decode_1 = ", decode_1)

master2 = b"master"
hash_2 = get_hash(master2)
print("hash_2 = ", hash_2)

decode_hash_2 = base64.standard_b64encode(master_hash.encode("utf-8"))
print("decode_hash_2 = ", decode_hash_2)
print("decode_hash_2_str = ", decode_hash_2.decode("utf-8"))

decode_pwd = decode_1.decode("utf-8")
print("decode_pwd_2_str = ", decode_pwd)

pwd_2 = decode_pwd.split(decode_hash_2.decode("utf-8"))[0]
print(pwd_2, "find")
# save_password(pwd_path, pwd_encode)

# code = load_password(pwd_path)
print(base64.standard_b64decode(pwd_2))
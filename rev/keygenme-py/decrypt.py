import hashlib

key_part_1 = "picoCTF{1n_7h3_|<3y_of_"
key_part_2 = ""
key_part_3 = "}"

bUsername_trial = b"ANDERSON"

def gen_key(username_trial):
    global key_part_2
    key_part_2 += hashlib.sha256(username_trial).hexdigest()[4]
    key_part_2 += hashlib.sha256(username_trial).hexdigest()[5]
    key_part_2 += hashlib.sha256(username_trial).hexdigest()[3]
    key_part_2 += hashlib.sha256(username_trial).hexdigest()[6]
    key_part_2 += hashlib.sha256(username_trial).hexdigest()[2]
    key_part_2 += hashlib.sha256(username_trial).hexdigest()[7]
    key_part_2 += hashlib.sha256(username_trial).hexdigest()[1]
    key_part_2 += hashlib.sha256(username_trial).hexdigest()[8]

gen_key(bUsername_trial)

print(key_part_1 + key_part_2 + key_part_3)

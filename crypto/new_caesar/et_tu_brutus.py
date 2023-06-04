import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

b16 = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"

def b16_decode(pt):
    dec_str = ""
    for i in range(int(len(pt)/2)):
        a = "{0:04b}".format(ALPHABET.index(pt[2*i:2*i+2][:-1]))
        b = "{0:04b}".format(ALPHABET.index(pt[2*i:2*i+2][-1:]))
        dec_char = int(a+b,2)
        dec_str += chr(dec_char)
    print(dec_str)
    print()
    return dec_str

def decrypt(ciphertext,key):
    plaintext = ''
    for i in range(len(ciphertext)):
        p = ALPHABET.index(ciphertext[i])
        k = ALPHABET.index(key[i%len(key)])
        c = (p - k) % 16
        plaintext += ALPHABET[c]
    return plaintext

for i in range(16):
    k = ALPHABET[i]
    pt = decrypt(b16, k)
    print(pt)
    b16_decode(pt)

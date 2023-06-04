import string
ALPHABET = string.ascii_uppercase

flag = "UFJKXQZQUNB"
# flag = "MTUFBSQOJGP"
key = "SOLVECRYPTO"

ans = ""
for i in range(len(flag)):
    temp = ALPHABET[(ord(flag[i]) - ord(key[i]))%26]
    print(temp)
    ans +=temp
print(ans)

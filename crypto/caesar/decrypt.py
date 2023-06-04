import string

flag = "ynkooejcpdanqxeykjrbdofgkq"
ALPHABET = string.ascii_lowercase
for i in range(26):
    dc = ""
    for j in flag:
        fl = ALPHABET.index(j)
        ky = i
        dc += ALPHABET[(fl + ky)%26]
    print(dc)

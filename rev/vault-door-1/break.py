random = {0: 'd', 29: '9', 4: 'r', 2: '5', 23: 'r', 3: 'c', 17: '4', 1: '3', 7: 'b', 10: '_', 5: '4', 9: '3', 11: 't', 15: 'c', 8: 'l', 12: 'H', 20: 'c', 14: '_', 6: 'm', 24: '5', 18: 'r', 13: '3', 19: '4', 21: 'T', 16: 'H', 27: '5', 30: '2', 25: '_', 22: '3', 28: '0', 26: '7', 31: 'e'}
password = dict(sorted(random.items()))
str = ""

for i in password:
    str += password[i]
print(len(str))
print(str)

list=[268,413,438,313,426,337,272,188,392,338,77,332,139,113,92,239,247,120,419,72,295,190,131]
map = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_']

x, y = 0, 1

def gcdExtended(a, b):
	global x, y
	if (a == 0):
		x = 0
		y = 1
		return b
	gcd = gcdExtended(b % a, a)
	x1 = x
	y1 = y
	x = y1 - (b // a) * x1
	y = x1
	return gcd

def modInverse(A, M):
	g = gcdExtended(A, M)
	if (g != 1):
		print("Inverse doesn't exist")
	else:
		res = (x % M + M) % M
		return res

str=""
for i in list:
    str+=map[modInverse(i%41,41)-1]

print(str)

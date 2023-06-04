from factordb.factordb import FactorDB

c = 421345306292040663864066688931456845278496274597031632020995583473619804626233684
n = 631371953793368771804570727896887140714495090919073481680274581226742748040342637
e = 65537

f = FactorDB(n)
f.connect()
lis = f.get_factor_list()
toi = (lis[0] - 1) * (lis[1] - 1)

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
		print("err")

	else:
		res = (x % M + M) % M
		return res

d = modInverse(e, toi)

def powmod(b,e,m):
	r = 1
	b = b % m
	if (b == 0):
		return 0
	while (e > 0) :
		if ((e % 2) == 1) :
			r = (r * b) % m
		e = e >> 1
		b = (b * b) % m
	return r

uc = powmod(c,d,n)
hexs = ""

def decTohex(n):
	if (n == 0):
		return "0"
	r = n % 16;
	global hexs
	hexs = hexs + hex(r)[2:]
	n //= 16
	decTohex(n)

decTohex(int(uc))
hexs = hexs[::-1]
print(bytearray.fromhex(hexs).decode())

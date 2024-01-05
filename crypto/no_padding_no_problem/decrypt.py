from pwn import *
from sage.all import *


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

conn = remote('mercury.picoctf.net',10333)
conn.recvuntil(b'n: ', drop=True)
n=int(conn.recvuntil(b'\ne: ', drop=True))
e=int(conn.recvuntil(b'\nciphertext: ', drop=True))
c=int(conn.recvuntil(b'\n', drop=True))
conn.recvuntil(b'decrypt: ', drop=True)
print(n,e,c)

r=power_mod(2,e,n)

conn.send(bytearray((str(c*r)+"\r\n").encode('ascii')))
conn.recvuntil(b'go: ')
m_=int(conn.recvuntil(b'\nGive', drop=True))

r_=modInverse(2, n)

uc=power_mod(m_*r_,1,n)
print(uc)

print(bytearray.fromhex(format(uc, 'x')).decode())

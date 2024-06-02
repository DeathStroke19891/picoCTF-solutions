enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽"
ans = ""

for i in enc:
    ans += chr(ord(i)>>8)
    ans += chr(ord(i)-((ord(i)>>8)<<8))

print(ans)

# Put some garbage into the netcat to bring the offset back to 50000
flag = "551e6c4c5e55644b56566d1b5100153d4004026a4b52066b4a5556383d4b0007"
key = "52176c4808036c4856006c485452476c4852056c4855066c4851516a6c485506"
result = ""
for i in range(32):
    fl = flag[2*i:2*i+2]
    ky = key[2*i:2*i+2]
    fl = int(fl,16)
    ky = int(ky, 16)
    result += chr(fl ^ ky ^ ord("0"))
print(result)

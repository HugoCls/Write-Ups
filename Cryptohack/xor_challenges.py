SECRET = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

_secret = int(SECRET, 16)

print(_secret)

for key in range(100000000000):

    flag = _secret ^ key

    hex_flag = hex(flag)[2:]

    print(key, bytes.fromhex(hex_flag))
    
    if "crypto" in str(bytes.fromhex(hex_flag)):
        print(key,hex_flag)

        print(hex(flag))
        break
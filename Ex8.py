a = "1234123456785678"
b = "*" * (len(a) - 4) + a[-4:]
print(b)
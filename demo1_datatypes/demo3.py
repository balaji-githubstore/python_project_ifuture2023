data = "Hello ashjdhshdsheeej World"

print(data[0])
print(data[5])

# prints 0 to end index -1
print(data[0:5])

print(data[1:])

print(data[-1:])
print(data[-2:])
print(data[-5:])

print(data[6:])

print(data[-5:])

print(data.index("World"))

print(data[19:])
print(data[data.index("World"):])

print(data.replace("World", "Hello"))

mail_id = "bala.88@gmail.com"

print(mail_id[0:8])
# print(mail_id[mail_id.index('@') + 1 : ])

print(mail_id.replace("World", "Hello"))
print(mail_id.index("@"))
print(mail_id[0:mail_id.index("@")])

mail_id = "bala.88@gmail.com"

res=mail_id.split("@")

print(res)
print(res[0])

print(mail_id.split("@")[0])


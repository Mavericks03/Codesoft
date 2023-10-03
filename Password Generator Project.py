import random

length = int(input("Enter the length of the password: "))
digits = '0123456789'
s_alphabets = 'abcdefghijklmnopqrstuvwxyz'
u_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''

for i in range(0, length):
    d = random.choice(digits)
    s = random.choice(s_alphabets)
    u = random.choice(u_alphabets)
    password = password + d + s + u

print(password)


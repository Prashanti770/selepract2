
secpwd = (('a','@'),('e','E'),('i','!'),('o','0'),('u','^'),('s','$'),('r','|'))

pwd = input("Enter password :   ")

for m,n in secpwd:
    pwd = pwd.replace(m,n)
print("Replaced password",pwd)


#Building a simple login and signup system using python

print('create account now')
username = input('enter username: ')
password = input('enter password: ')

print('your account has been created successfully')
print('login now!')

username2 = input('enter username: ')
password2 = input('enter password: ')

if username == username2 and password == password2:
    print('logged in successfully')
else:
    print('invalid credentials')
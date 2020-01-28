#Sign Up

import getpass

usr = input('Username: ')
while True:
    psd = getpass.getpass('Password: ')
    psd_again = getpass.getpass('Password again: ')
    if psd == psd_again:
        break
    else:
        print('Passwords do not match')

#Add credentials to "database"

db1 = []
db2 = []

db1.append(usr)
db2.append(psd)

#Log in

user_input = input("Username : ")
password_input = getpass.getpass("Password: ")

#Authentication

auth = False

if user_input in db1 and password_input in db2:
    aux = 0
    for i in db1:
        if i == user_input:
            break
        aux += 1
    if db2[aux] == password_input:
        auth = True

if auth == False:
    print('Wrong credentials')
else:
    print('Welcome, %s !' % user_input)

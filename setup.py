import json
import os
import hashlib
import getpass

if __name__ == "__main__":
    newPath = os.getcwd()
    print("Your current working directory is:")
    print(newPath + "\n")
    choice = input("Would you like to use this path (y/n): ")
    if choice != 'y' and choice != 'Y' and choice != 'yes':
        newPath = input('Please enter your new path:\n')

    with open('app.py', 'r') as file:
        lines = file.readlines()

    index = 0
    for line in lines:
        if 'appDir = '  in line:
            break
        index += 1
    
    lines[index] = 'appDir = \'' + newPath + '\'\n'
    
    with open('app.py', 'w') as file:
        file.writelines(lines)

    with open('admin.json', 'r') as admin:
        data = json.load(admin)

    
    username = str(hashlib.sha256(input('Please enter an admin username: ').encode()).hexdigest())
    password = str(hashlib.sha256(getpass.getpass('Please enter an admin password: ').encode()).hexdigest())
    passeord_re_enter = str(hashlib.sha256(getpass.getpass('Please re-enter the password: ').encode()).hexdigest())

    if password == passeord_re_enter: 
        data['username'] = username
        data['password'] = password
        print("Username and password have been updated")
    else:
        print("Passwords do not match, username and password are unchanged")

    with open('admin.json', 'w') as admin:
        json.dump(data, admin, indent=2)

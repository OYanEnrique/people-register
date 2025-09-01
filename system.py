from interface import *
from archive import *
from time import sleep

fil = 'archive.txt'

if not archiveexists(fil):
    createarchive(fil)

while True:

    answer = menu(['See registered users', 'Register new user', 'Exit'])
    if answer == 1:
        readfile(fil)
    elif answer == 2:
       header('New registration')
       name = input("Enter the name: ")
       age = input("Enter the age: ")
       registration(fil, name, age)
    elif answer == 3:
       header('Exiting the system')
       sleep(1)
       break
    else:
        print("\033[31mError! Please enter a valid option.\033[0m")

    sleep(1.5)
from interface import header

def archiveexists(name):
    try:
        with open(name, 'rt') as f:
            pass
    except FileNotFoundError:
        return False
    return True

def createarchive(name):
    try:
        with open(name, 'wt+') as f:
            f.write('')
    except:
        print("\033[31mAn error occurred while creating the archive.\033[0m")
    else:
        print(f"\033[32mArchive '{name}' created successfully.\033[0m")

def readfile(name):
    try:
        with open(name, 'rt') as file:
            for line in file:
                data = line.split(';')
                data[1] = data[1].replace('\n', '')
                print(f"\033[34mName:\033[0m {data[0]:<30} \033[34mAge:\033[0m {data[1]:>3} years")
    except:
        print("\033[31mAn error occurred while reading the archive.\033[0m")

def registration(fil, name='unknown', age=0):
    try:
        with open(fil, 'at') as f:
            f.write(f"{name};{age}\n")
    except:
        print("\033[31mAn error occurred while registering the user.\033[0m")
    else:
        print(f"\033[32mUser '{name}' registered successfully.\033[0m")


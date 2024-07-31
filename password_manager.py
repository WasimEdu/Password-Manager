# Created by: Wasim

master_pwd = input("What is the mster password: ")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", 'a') as f:
        f.write(name + " | " + pwd + "\n")

def view():
    
    with open("password.txt", "r") as f:
        for lines in f.readlines():
            print(lines.strip())


while True:
    mode = input("Would you like to add new password or view (add/view). type q to quit: ").lower()

    if mode == "q":
        break

    if mode == "add":
        add()

    elif mode == "view":
        view()

    else:
        print("Invalid mode!")

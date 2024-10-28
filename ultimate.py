import os
from time import sleep
try:
    from datetime import datetime
except:
    os.system("pip install datetime")
    from datetime import datetime


now = datetime.now()
dt_string = now.strftime("%d-%m-%Y")

def create(name):
    if not os.path.exists(name):
        os.mkdir(name)
        
def changer():
    tokens = open("tokens.txt", "r").read().splitlines()
    for tokenss in tokens:
        token = tokenss.split(":")[2]
        create("Log")
        create(os.path.join("Log/", dt_string))
        with open(f"Log/{dt_string}/tokens.txt","a+") as file:
            file.write(f"{token}\n")
        
            
def menu():
    os.system("cls")
    print("""Email:pass:token to token (y/n)""")
    print()
    choice = input("Whats your choice: ")
    if choice == "y":
        changer() 

    else:
        print("Wrong choice!")
        sleep(1)
        menu()

    print("Tokens Formatted!")
    sleep(1)
    exit()
menu()
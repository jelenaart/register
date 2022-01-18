from module1 import *
users=["biba"]
passwords=["boba"]
valik=""
while True:
    try:
        valik=int(input("Palun valige sisselogimise viis (1-signup), (2-signin), (3-proovida random moodul), (4-quit)"))
        if valik==1:
            signup(users,passwords)
        elif valik==2:
            signin(users,passwords)
        elif valik==3:
            ran(passwords)
        elif valik==4:
            quit
        else:
            print("Midagi on valesti. Palun proovige veel kord!")
    except ValueError:
        print("Proovige veel kord!")

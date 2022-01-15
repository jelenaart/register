import module1
users=["biba"]
passwords=["boba"]
valik=""
valik=int(input("Palun valige sisselogimise viis (1-signup), (2-signin), (3-random), (4-quit)"))
if valik==1:
    signup()
elif valik==2:
    signin()
elif valik==3:
    random()
elif valik==4:
    quit
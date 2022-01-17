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
def signup():
    user=input("Valige kasutajanimi: ")
    password=input("Valige salasona: ")
    if user in users:
        print("See kasutaja on juba registreeritud!")
    else:
        users.append(user)
        passwords.append(password)
        print("Kasutajanimi: ", user)
        print("Parool: ", password)
def signin():
    user=input("Palun teie kasutajanimi: ")
    password=input("Palun teie parool: ")
if user in users and users.index(user) == passwords.index(password):
     print ("Olete sisseloginud!")
else:
     print("User doesn't exist or wrong password!")
def random():
    str0=".,"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    print(ls)
    login = ''.join([random.choice(ls) for x in range(12)])
    passw = ''.join([random.choice(ls) for x in range(12)])
    print("Siin on teie kasutajanimi ja parool!")
    print("kasutajanimi: " ,login, "parool: " ,passw)
while valik!= "quit":
     valik()



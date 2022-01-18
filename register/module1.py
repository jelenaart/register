def signup(users:list,passwords:list):
    user=input("Valige kasutajanimi registreerimiseks: ")
    print("Kas te soovite ise parooli valida(1) või genereerida(2)?")
    valik=input()
    if valik=="2":
        password=ran()
        print(f"Teie genereeritud parool on: {password}")
    elif valik=="1":
        password=input("Valige salasona registreerimiseks: ")
        control=passcontrol(password)
        while control==False:
            print("Teie salasõna peaks sisaldama alltähed, suured tähed, numbrid")
            password=input("Palun teie parool: ")
            control=passcontrol(password)
            if control==True:
                break
    if user in users:
        print("See kasutaja on juba registreeritud!")
    else:
        users.append(user)
        passwords.append(password)
        print("Kasutajanimi: ", user)
        print("Parool: ", password)
def signin(users:list,passwords:list):
    user=input("Palun teie kasutajanimi: ")
    password=input("Palun teie parool: ")
    if user in users and users.index(user) == passwords.index(password):
         print ("Olete sisseloginud!")
    else:
         print("Kasutajanimi ei leitud või vale parool!")
def ran(passwords:list):
    str0=".,"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    print(ls)
    login = ''.join([ran.choice(ls) for x in range(12)])
    passw = ''.join([ran.choice(ls) for x in range(12)])
    print("Siin on teie kasutajanimi ja parool!")
    print("kasutajanimi: " ,login, "parool: " ,passw)
    return passw,login
def passcontrol():
    passcontrol=list(passwords)
    p=False
    for i in passcontrol:
        if i.isdigit():
            p=True
        if i.isalpha():
            p=True
        if i.isupper():
            p=True 
        if i.islower():
            p=True
    return p

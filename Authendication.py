def check():

    username = input("enter your username:")
    password = input("enter your password:")

    file=open('Authendication.txt', 'r')#to get the stored username&password from Authendication.txt

    fusername = file.readline()
    fpassword = file.readline()
    fusername = fusername.strip()

    if username == fusername and password == fpassword:
        return True
    else:
        return False

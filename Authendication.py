def check(username, password):
    with open('Authentication.txt', 'r') as file:
        valid_username = file.readline().strip()
        valid_password = file.readline().strip()

        if username == valid_username and password == valid_password:
            return True
        else:
            return False

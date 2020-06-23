import username
user_name = username()
file = open("UserName.get", "w")
file.write('{}'.format(user_name))
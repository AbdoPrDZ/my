import os
import username
# Get Programe Data Link
position=os.getcwd()
file= open('linkis.get','w')
file.write('"{}"'.format(position))
# Get PC UserName
user_name = username()
file = open("UserName.get", "w")
file.write('{}'.format(user_name))
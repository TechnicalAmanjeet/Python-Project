import os
file_name=input(" Enter file name  : ")
path="/etc/yum.repos.d/"
ip="mkdir "+ path + file_name + ".repo"
if not(os.system(ip)):
  print(file_name , " file created successfully... ")

input("preess enter to go next...")

path = path + file_name + ".repo"

filename = path + file_name + ".repo"

dvdpath = input("Enter the dvd path ( by default press 1 ) : ")
if dvdpath == '1':
  dvdpath = "/app"

content ="[App1]\nbaseurl=file:///app/AppStream\ngpgcheck=0\n\n[App2]\nbaseurl=file:///app/BaseOS\ngpgcheck=0"

print(content)

input("Press enter to execute above statement...")

f=open(filename,'a')
f.write(content)
f.close()

os.system("yum repolist")

print("\n yum configured successfull...")
import os

os.system("clear")
print("\n\t\t**************** installation of httpd software *************")

mnt=input("""\n\n
        Press 0 : rhel dvd file already mounted
        press other key : if its not mounted
        \n
        : """)

print("\n ", mnt)

if(not(mnt)==0):
  os.system("clear")
  print("\n\t\t************ Mounting of rhel dvd going on **************")
  
  print("\n Before going to next section make sure you have attached default rhel dvd to your os / virtualbox..")
  
  input("\n press enter if you have attached it....")
  
  file_name=input("\n\n Enter file name to mount : ")
  input("/n" + file_name +" file created successfully... press enter to go next...")
  
    
  file_name="/"+file_name
  
  mounted_file=file_name
  
  z= "mkdir "+file_name
  
  os.system(z)

  file_name_to_mount=input("/n Enter the file name to mount ( for rhel dvd type 1 for ( /dev/sr0 ) : ")
  
  print("\n" , file_name)

  if int(file_name_to_mount)==1:
    inp = "mount /dev/sr0 " + file_name
    file_name_to_mount="/dev/sr0"
  else:
    inp="mount "+ file_name_to_mount + " " + file_name

  if(os.system(inp)==0):
    print("\n we have successfully mounted the file "+ file_name_to_mount +" to "+file_name+" ...")

input("\n Press Enter to go to next section of installation.... ")

os.system("clear")

print("\n\t\t**************** installation of httpd software *************\n\n")


os.system("yum repolist")

x = input("press 0 . if there is Appstream and BaseOs software. i.e if yum repo is configured press other key if No Repository is Available : ")

if(not(x)==0):
  os.system("clear")

  print("\n\t\t**************** yum rep configuration *************\n\n")
  file_name=input(" Enter file name  : ")
  path="/etc/yum.repos.d/"
  ip="touch "+ path + file_name + ".repo"
  if not(os.system(ip)):
    print(file_name , " file created successfully... ")

  input("preess enter to go next...")

  
  filename = path + file_name + ".repo"
  
  print("\n\n filename with path : " , filename)

  dvdpath = input("Enter the dvd path ( by default press 1 ) : ")
  if dvdpath == '1':
    dvdpath = mounted_file

  content ="[App1]\nbaseurl=file://"+mounted_file+"/AppStream\ngpgcheck=0\n\n[App2]\nbaseurl=file://"+mounted_file+"/BaseOS\ngpgcheck=0"

  print(content)

  input("Press enter to execute above statement...")

  f=open(filename,'a')
  f.write(content)
  f.close()

  os.system("yum repolist")
  
  print("\n ************** yum Configured Successfully ************")
  

input("\n Press enter to go and install httpd software...")

os.system("clear")

print("\n\t\t**************** installation of httpd software *************\n\n")

if(not(os.system("rpm -q httpd"))==  0):

    os.system("yum install httpd")

    input("\n httpd software installed press enter to move...")

    os.system("systemctl start httpd")

    input("\n  httpd webserver started press enter to move next...")
else:
    print("\n Httpd software already installed...")

print("\n\n *************** success ****************")
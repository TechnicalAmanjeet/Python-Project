import  os
file_name= "/" + input("/n Enter the file name : ")
inp= 'mkdir '+ file_name;

os.system(inp)

input("/n" + file_name+" file created successfully... press enter to go next...")

file_name_to_mount=input("/nEnter the file name to mount ( for default type 1 ) : ")

if int(file_name_to_mount)==1:
  inp = "mount /dev/sr0 " +file_name
  file_name_to_mount="/dev/sr0"
else:
  inp="mount "+ file_name_to_mount + " " + file_name

if(os.system(inp)==0):
  print("we have successfully mounted the file "+ file_name_to_mount +" to "+file_name+" ...")
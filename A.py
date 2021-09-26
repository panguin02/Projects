def encryptor(Filename,key):
    file=open(Filename,"rb")
    content=file.read()
    file.close()
    content=bytearray(content)
    for index,value in enumerate(content):  
        content[index]=value ^ key
    
    file=open("GE"+Filename,"wb")
    file.write(content)
    file.close()


def decryptor(Filename,key):
    file=open(Filename,"rb")
    content=file.read()
    file.close()
    content=bytearray(content)
    for index,value in enumerate(content):
        content[index]=value ^ key
    
    file=open(Filename,"wb")
    file.write(content)
    file.close()

choice=""
while choice!=3:
    print("select choice")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Quit")
    choice=input()
    if choice=="1" or choice=="2":
        key=int(input("Enter the key"))
        Filename=input("enter the file name")
    if choice=="1":
        encryptor(Filename,key)
    if choice=="2":
        decryptor(Filename,key)

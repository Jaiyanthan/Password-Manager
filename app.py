import base64

 # initial text value to genrate a set of random data
key = "This is a secret key"

# function to encrypt the data
def encrypt(text):

        # getting the plain text
        print("Enter the message to be encrypted")
        message = text

        # empty list of encrypted data
        encrypt = []

        for i in range(len(message)):
            # creating a set of numbers from the text
            key2 = key[i % len(key)]
            # appending the generated randomly jumbled data to the array
            encrypt.append(chr((ord(message[i]) + ord(key2)) % 567))
        # encrypted data    
        encryption = base64.urlsafe_b64encode("".join(encrypt).encode()).decode()
        return encryption
        
# function to decrypt the data
def decrypt(text):
            
        decrypt = []
        # getting the encrypted data
        input = text
        message = base64.urlsafe_b64decode(input).decode()
        # reversing the process
        for i in range(len(message)):
            key2 = key[i % len(key)]
            decrypt.append(chr((567 + ord(message[i]) - ord(key2)) % 567))
        # getting the decrypted data    
        return("".join(decrypt))



# creating an empty instance
menu = ""

# While loop
while menu != "1" and menu != "2":
    
    menu = input("Would like to save a new password or read the old ones ?"
            "\n1. Save new Password"
            "\n2. Read old Passwords"
            "\n3. Exit"
     )

    if menu == "1":
         application = input("Enter the name of the appication ")
         username = input("Enter your username ")
         password = input("Enter the respective password ")
         file  = open("passwordData.txt", "a")
         file.write(encrypt(application) + ' | ' + encrypt(username) + ' | ' + encrypt(password) + '\n')
         file.close()
    
    if menu == "2":
          masterpassword= input("Enter your master password")
          if (masterpassword == "jaiyantan3057@tn.com1"):
                file = open("passwordData.txt", "r")
                print("Application\tUsername\tPassword\t") 
                for i in file:
                        data = i.split(' | ')
                        print(decrypt(data[0])+ "\t\t" +decrypt(data[1])+ "\t" + decrypt(data[2]))
          else:
              print("wrong password")
    if menu == "3":
        exit()            

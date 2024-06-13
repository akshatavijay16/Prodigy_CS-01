#Implemention of caesar cipher 

#Encryption
def encrypt(msg,key):
    ans=""
    for i in range(len(msg)):
        ch=msg[i]
        if ch=="":
            ans+=''
        ans+=chr((ord(ch)+key-65)%26+65)
    return ans

#decryption
def decrypt(msg,key):
    ans=""
    for i in range(len(msg)):
        ch=msg[i]
        if ch=="":
            ans+=""
        ans+=chr((ord(ch)-key-65)%26+65)
    return ans

#user input
msg=input("Enter a string :")
msg=msg.upper()

key=int(input("Enter number to  get shifted:"))
et=encrypt(msg,key)
print("encryption",et)

dt=decrypt(et,key)
print("decryption",dt)
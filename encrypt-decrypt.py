#function to encrypt
def encrypt(msg,key):
    encrypted_msg = str(ord(msg[0])+key)+msg[len(msg)-2:0:-1]+str(ord(msg[len(msg)-1])+key)
    
    print("Original message: ", msg)
    print("Encrypted message: ", encrypted_msg)
    return encrypted_msg
    

def decrypt(encrypted_msg,key):
    decrypted_msg = str(chr(int(encrypted_msg[0:3])-key))+encrypted_msg[len(encrypted_msg)-4:2:-1]+str(chr(int(encrypted_msg[-3:])-key))
    print("Decrypted message: ", decrypted_msg)
    
#main
msg = "My name is salman"
key = 28
encrypted_msg = encrypt(msg,key)
decrypt(encrypted_msg,key)
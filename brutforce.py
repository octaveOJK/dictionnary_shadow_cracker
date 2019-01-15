import random
import crypt
import hashlib
from passlib.hash import md5_crypt

def testPass(cryptPass):

    characters = "abcdefghijklmpnoqrstuvwxyz"
    length = 6
    while True:
        pw = ""

   #Generating Section
        for i in range(length):
            next_index = random.randrange(len(characters))
            pw = pw + characters[next_index]
            cryptWord = hashlib.md5(pw.encode("utf-8")).hexdigest()
        #print(bytes(cryptWord, 'utf-8'), bytes(cryptPass[:-1], 'utf-8'))
        if cryptWord == cryptPass :
            print("[+] mot de passe trouve : "+pw+"\n")
    print("[-] mot de passe introuvable, agrandit ton dictionnaire.\n")

def main():
    passFile = open('shadow.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("[*] test du mot de passe pour : "+user)
            testPass(cryptPass)

if __name__ == "__main__":
    main()

import crypt
import hashlib
from passlib.hash import md5_crypt

def testPass(cryptPass):
	dictFile = open('dico.txt','r')
	for word in dictFile.readlines():
		theWord = word.strip('\n')
		cryptWord = hashlib.md5(theWord.encode("utf-8")).hexdigest()
		#print(bytes(cryptWord, 'utf-8'), bytes(cryptPass[:-1], 'utf-8'))
		if cryptWord == cryptPass[:-1]:
			print("--> mot de passe trouve : "+word+"\n")
			return
	print("--> mot de passe introuvable, agrandit ton dictionnaire.\n")
def main():
	print()
	passFile = open('/home/octave/Bureau/crack/crackv1/shadow.txt')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print("--> test du mot de passe pour : "+user)
			testPass(cryptPass)
if __name__ == "__main__":
	main()

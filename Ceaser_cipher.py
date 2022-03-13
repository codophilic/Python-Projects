#Here you can encrypt and decrypt alphabets of capital and small as well as numbers or digit
def correction(message,k,sign_key):
	check=0# checking all the things are correct or not for both encryption and decryption
	while(check!=1):
		for m in message:
			if m.isalnum()==False:#checks for alphanumeric
				message=input("ENTER YOUR MESSAGE WITHOUT SPACE AND SPECIAL CHARACTERS (#,$,_,&,@,-) :")
				break
		check=1
	if sign_key=="e" : key,z,a=k,0,'POSTIVE'
	else: key,z,a=k,0,"NEGATIVE"
	while(check!=2):
		if (key>=z and a=="POSTIVE") or(key<=z and a=="NEGATIVE"):
			check+=1		
		else:
			key=int(input("ENTER {s} NUMBER WITHOUT DECIMAL POINT KEY :".format(s=a)))
		
	return message, key
		
  
def message_encrypt_or_decrypt( message,key,c):
	st=""
	s=-1 if c=='e' else 1
	for m in message:
		if 65<=ord(m) and ord(m)<=90: st+=encrypt_or_decrypt(m,key,65,90,s*26)
		elif 97<=ord(m) and ord(m)<=122: st+=encrypt_or_decrypt(m,key,97,122,s*26)
		else: st+=encrypt_or_decrypt(m,key,48,57,s*10)
	return st


def encrypt_or_decrypt(message,key,a,z,t):
	key=key-1 if key%t==0 and t<0 else key#if message is undershift or overshift
	key=key+1 if key%t==0 and t>0 else key
	if(a<=ord(message)+key and ord(message)+key<=z):
		return chr(ord(message)+key)
	#exception for 26,10power
	else:# if message is overshift or undershift
		i=1
		while(True):
			n=key+ord(message)+t*i
			if a<=n and n<=z:
				return chr(n)
			i+=1
   
   
message=input("ENTER THE MESSAGE TO BE ENCRYPTED :")
key=int(input("ENTER YOUR KEY :"))
message,key=correction(message,key,"e")
#after checking all things are correct
if key>0: 	st=message_encrypt_or_decrypt(message,key,'e') 
print("ENCRYPTED STRING IS :"+st)
#decryption part 
message=input("ENTER THE ENCRYPTED STRING WHICH IS TO BE DECRYPTED :")
key=int(input("ENTER THE INVERT OF THE KEY :"))
message,key=correction(message,key,"d")
#after checking again all things are correct 
if key <0: st=message_encrypt_or_decrypt(message,key,'d')
print("DECRYPTED MESSAGE IS :"+st)

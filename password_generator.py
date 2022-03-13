import random


def numbers(N):#checking the no. is positive or not
	while (True):
		if N<0:
			N=int(input("ENTER A POSTIVE NO. :"))
		else :
			return N	  

  
def invent():#creates and gives a string off random,digit,small & large alphabets
	a={1:list(map(chr,range(48,58))),2:list(map(chr,range(97,123))),3:list(map(chr,range(65,91)))}
	b=""
	for i,j in a.items():
		b+=random.choice(j)
	return b


def simple_generator(l,digit,small,big):#e.g...AAaa123...etc
	password=""
	for i in range(digit):
		b=invent()
		password+=b[0]
	for j in range(small):
		b=invent()
		password+=b[1]
	for k in range(big):
		b=invent()
		password+=b[2]
	return "".join(reversed(password))	

  
def complex_generator(l,digit,small,big):#e.g ..A12aA3a,1A3aaA2..etc
			password=""
			d,a,A,j=digit,small,big,l
			while(j!=0):
				o=0
				while(o==0):
					p=random.choice(invent())
					if 48<=ord(p) and ord(p)<=57 and d!=0:
						r,o,d=1,1,d-1
					elif 97<=ord(p) and ord(p)<=122 and a!=0:
						r,o,a=1,1,a-1
					elif 65<=ord(p) and ord(p)<=90 and A!=0:
						r,o,A=1,1,A-1
					else :
						r,o=0,1
				if r==1:
					j-=1
					password+=p
			return password	

			
N=int(input("ENTER THE NO. OF PASSWORD REQUIRED :"))
N=numbers(N)
l=int(input("ENTER THE LENGTH OF PASSWORD REQUIRED :"))
l=numbers(l)
while(True):#matching the length
	digit=int(input("ENTER THE NO. OF DIGITS REQUIRED IN PASSWORD :"))
	digit=numbers(digit)
	small=int(input("ENTER THE NO. OF SMALL LETTERS REQUIRED IN PASSWORD :"))
	small=numbers(small)
	big=int(input("ENTER THE NO. OF CAPITAL LETTERS REQUIRED IN PASSWORD :"))
	big=numbers(big)
	if digit+small+big!=l: print("!!!DIGITS,SMALL LETTERS AND CAPITAL LETTERS DO NOT MATCH WITH LENGTH OF PASSWORD, SO PLEASE RE-ENTER CAREFULLY !!!")
	else :
		break
ind=int(input("ENTER THE FOLLOW INDEX NO. \n 1. SIMPLE PASSWORD \n 2. COMPLEX PASSWORD \n 3. BOTH \n "))
if ind==1:#switch case
	for i in range(N):
		print(simple_generator(l,digit,small,big))
elif ind==2:
	for i in range(N):
		print(complex_generator(l,digit,small,big))
else :
	print("SIMPLE PASSWORD\n :")
	for i in range(N):
		print(simple_generator(l,digit,small,big))
	print()
	print("COMPLEX PASSWORD\n :")
	for i in range(N):
		print(complex_generator(l,digit,small,big))

from itertools import permutations

def printing(c,N):
	i=0
	print()
	for i in range(N):
		for j in range(N):
			if i==r[i] and j==c[i]:
				print('Q',end=" ")
			else:
				print('•',end=" ")
		print()	
def upgoing_right_left(x,y,d):
	cord=[]
	while(0<=x and y<=N-1):
		if d=='r':x,y=x-1,y+1
		if d=='l':x,y=x-1,y-1
		l=[x,y]
		cord.append(l)
	for ci in cord:
		for i in r:
			if ci[0]==i and ci[1]==c[i]:
				return 'no' 
	return 'yes'
N=int(input("ENTER THE NO. OF QUEENS :"))
if N<4:
	print("THERE ARE NO POSSIBLE COMBINATIONS FOR {n}".format(n=N))
combo,breakc=0,0
if N>8:
	print("AFTER 8 QUEENS THE COMBINATION WILL BE TOO LONG SO PLEASE ENTER ONLY REQUIRED NUMBER OF COMBINATIONS")
	combo=int(input("ENTER HERE :"))
possibilities=list(permutations(range(N)))
r=list(range(N))
subseq_poss,final_column=1,[]
while(subseq_poss<len(possibilities)):
	c,l,count=list(possibilities[subseq_poss]),N-1,0
	while(l>0):
		check_left=upgoing_right_left(r[l],c[l],'l')
		if check_left=='yes':
			check_right=upgoing_right_left(r[l],c[l],'r')
			if check_right=='yes':
				count,l=count+1,l-1
				if count==N-1:
					final_column.append(c)
					combo-=1
					if N>8 and combo==0:
						breakc=1
						break										
			else :break
		else :break
	if N>8 and breakc==1:
		break
	subseq_poss+=1
for c in final_column:
	printing(c,N)
if N>3 and N<9:
	print("TOTAL NO. OF POSSIBLE COMBINATIONS IS {n}".format(n=-combo))
			
		
	

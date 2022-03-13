import pandas as pd 
df= pd.read_csv('Singapore_Residents.csv')

#In the excel sheet there are records of total residents,Malays,Chinese,Indian and Ethnic groups of both males and females	
c,male,female=0,[],[]#creating an array of male and female having names of level_1

#print(df['level_1'])
for i in df['level_1']:#consider first 15 row or 2000 columns records to store the headings of level_1 in the two list as shown 
	if c in [1,4,7,10,13]:
		male.append(i)
	if c in [2,5,8,11,14]:
		female.append(i)
	if c==15: break
	c+=1
#print(male)
#print(female)
ey=pd.DataFrame({"Years":['2000-2001','2001-2002','2002-2003','2003-2004','2004-2005','2005-2006','2006-2007','2007-2008','2008-2009','2009-2010','2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018']})
def checkloops(y):#checks if the year is in range and positive
	while(True):
		if y>0 and (1999<y and y<2019): return y
		else :
			y=int(input("PLEASE ENTER A POSITIVE NUMBER . THE YEAR IN THE DATA CONTAIN IS FROM 2000 TO 2018 ,SO PLEASE RE-ENTER CAREFULLY :"))
   
   
def add_value(y):#Adding the value of the year
	sum,a=0,df[df['year']==y]
	for i in a["value"]:
		sum+=i
	return sum


def particular(sy,ly,ind):#Switch Case Statements
	cal=[]
	for i in ey[male[ind-1]]:
		cal.append(i)
	print("THE GROWTH OF MALE POPULATION IN '{n}' IS : {s}".format(n=male[ind-1],s=sum(cal[(sy%2000):ly%2000])))
	cal.clear()
	for i in ey[female[ind-1]]:
		cal.append(i)
	print("THE GROWTH OF FEMALE POPULATION IN '{n}' IS :{s}".format(n=female[ind-1],s=sum(cal[(sy%2000):ly%2000])))
 
 
def change(n,s):#Consecutive years
	m,diff=[],[]
	a=df.set_index('level_1')#set index as level_1 since level 1 contains each details
	#print(a)
	a1=a.loc[n]#access only particular details ("n") 
	#print(a1)
	for i in a1['value']:
		m.append(i)
	for j in range(18):#2018-1999-1(getting the diff of consecutive)
		diff.append(m[j+1]-m[j])
	ey[n]=diff
 
 
y=int(input("ENTER THE YEAR IN WHICH YOU NEED THE VALUE :"))#calculates the nuemrical values present in that particular year
y=checkloops(y)
print()
print("THE TOTAL ADDITION OF VALUE OF {Y} is : {s}".format(Y=y,s=add_value(y)))
print()
print("THE CHANGE IN THE POPULATION GROWTH OF MALE AND FEMALES IN EVERY YEAR IS :")
print()
for i in male:#Consecutive year change in population of male 
	change(i,'male')
for i in female:# Consecutive year change in population of female
	change(i,'female')
print("				      FOR GROWTH IN POPULATION OF MALES")
print()
print(ey[ey.columns[0:6]])
print()
print("				      FOR GROWTH IN POPULATION OF FEMALES")
print()
print(pd.concat([ey[ey.columns[:2]],ey[ey.columns[6:]]],axis=1,sort=False))
print()
print("(NOTE-----'NEGATIVE SIGN INDICATES POPULATION WAS DECREASED')")
print()
print("TO KNOW THE CHANGE IN POPULATION BETWEEN ANY TWO YEAES")
print()
sy=int(input("ENTER THE STARTING YEAR :"))
sy=checkloops(sy)
print()
ly=int(input("ENTER THE LAST YEAR :"))
ly=checkloops(ly)
print()
print("SELECT ANY ONE OF THE CATEGORIES AND ENTER THE INDEX VALUE :")
print()
ind=int(input("1.RESIDENTS\n2.MALAYS\n3.CHINESE\n4.INDIANS\n5.OTHER ETHNICS GROUPS\n6.All OF THESE\n"))
if sy>ly: sy,ly=ly,sy#if Starting year is greater than the ending year
if ind==6:
	for i in range(1,6):
		particular(sy,ly,i)
else :
	particular(sy,ly,ind)
print()
print("(NOTE:-----'NEGATIVE SIGN INDICATES POPULATION WAS DECREASED')")
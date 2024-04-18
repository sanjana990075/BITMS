#first program
'''if(5>10):
    print("yes")
else:
    print("no")'''

#2nd prgm
'''age1=int(input("enter age1"))
age2=int(input("enter age2"))
if(age1>age2):
    print("age1 is greater")
    print(age1)
else:
    print("age2 is greater")
    print(age2)'''

#3rd prgm
'''org_email="rsanjana9008@gmail.com"
org_password="rsanjana@2004"
emailid=input("enter email id")
password=input("enter password")
if((password==org_password)&(emailid==org_email)):
    print("login succesfull")
else:
    print("invalid password")'''

#4th prgm
'''org_email="rsanjana9008@gmail.com"
org_password="sanjana@2004"
emailid=input("enter email id")
password=input("enter password")
if(org_email==emailid):
    if(org_password==password):
        print("login succesfull")
    else:
         print("login failed due to incorret password")
else:
       print("login failed dur to incorrect email id")'''

#5th prgm
'''org_email="rsanjana9008@gmail.com"
org_password="rsanjana@2004"
emailid=input("enter email id")
password=input("enter password")
if((password==org_password)&(emailid==org_email)):
    print("login succesfull")
    org_otp=2345
    otp=int(input("enter otp"))
    if(org_otp==otp):
        print("transaction succesfull")
    else:
        print("transcation failed due to invalid otp")
else:
    print("login failed")'''

#6th prgm using ternary operator
'''num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
print("num1 is greater" if((num1>num2)&(num1>3)) else "num2 is greater" if(num2>num3) else "num3 is greater")'''

#7th prgm
'''print(chr(3256)+chr(3202)+chr(3228)+chr(3240))'''

#8th prgm
'''num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))
num5 = int(input("Enter num5: "))

result = ("num1 is greater" if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5 else
          "num2 is greater" if num2 > num3 and num2 > num4 and num2 > num5 else
          "num3 is greater" if num3 > num4 and num3 > num5 else
          "num4 is greater" if num4 > num5 else
          "num5 is greater")

print(result)'''

#9th prgm
'''print(ord("s"))'''
#ordinal method is used to convert the char into value

#10th prgm
'''for i in range(ord('a'),ord('z')):
    print(ord(chr(i)))
for i in range(ord('A'),ord('Z')):
    print(ord(chr(i)))'''

#11th prgm
'''for i in range(1,6):           
    for i in range(1,i+1):
        print('*',end=' ')
    print()'''

#12th prgm
'''for i in range(1,6):           
    for i in range(1,6):
        print('*',end=' ')
    print()'''

#13th prgm
'''for i in range(1,6):           
    for i in range(1,i+1):
        print(i,end=' ')
    print()'''

#14th prgm
'''for i in range(65,91):           
    for j in range(65,i+1):
        print(chr(i),end=' ')
    print()'''
 
#15th prgm
'''for i in range(1,11):
    print(i/10)'''
    
#16th prgm
'''def leap():
    n=int(input("enter the year"))
    if((n%4==0)&(n%400==0)):
        print("its leap year")
    else:
        print("not a leap year")
          
leap()'''

#17th prgm
'''sanjana=[]
n=int(input("enter size"))
for i in range(0,n):
    ele=int(input("enter the ele"))
    sanjana.append(ele)
print(sanjana)'''

#18th prgm
'''list1=["sanajna"]
list2=["siri"]
list3=list1+list2
print(list3)
print(type(list3))
print(list3*2)
print(len(list3))'''

#19th prgm(sum of list ele)
'''sanju=[10,20,30,40,50]
sum=0
for i in sanju:
    sum=sum+i
print(sum)'''

#20th prgm(ending desired no's)
'''sanju=[10,25,37,40,57,65]
sum=0
for i in sanju:
    if(i%10==5):
        print(i)'''

#21th prgm(remove duplicate ele in list)
'''list1=[10,20,30,40,50,10,30,40,60]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)   '''

#22nd(checking common ele in list)
'''list1=[]
list2=[]
n1=int(input("enter size of list1"))
for i in range(0,n1):
    ele=int(input("enter ele"))
    list1.append(ele)
n2=int(input("enter size of list1"))      
for i in range(0,n2):
     ele=int(input("enter ele"))
     list2.append(ele)
            
for i in list1:
    for j in list2:
        if(i==j):
           print(i)'''

#23rd prgm
'''get 5 values from user store in list now the goal is out of 5 ele which are prime no and leap year
2004,1996,17,10,85'''
'''def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_leap_year(year):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return True
    else:
        return False

list1 = [2004, 1996, 17, 10, 85]

for num in list1:
    prime_check = "prime" if is_prime(num) else "not prime"
    leap_year_check = "leap year" if is_leap_year(num) else "not leap year"
    print(num, "is", prime_check, "and", leap_year_check)'''

#tupple operations
'''tuple1=()
n1=int(input("enter tuple1 size"))
for i in range(0,n1):
    ele=int(input("enter ele"))
    tuple[i]=ele
print(tuple1)
print("accesing through indices")
print(tuple1[0],tuple1[1],tuple1[2],tuple1[3])
print("accesing through negative indices")
print(tuple1[-1],tuple1[-2],tuple1[-3],tuple1[-4])
tuple2=(10,20,30,40)
print(tuple1==tuple2)
#we can not change values
#tuple1[0]=(20)
print(tuple1[1:3])
print(tuple1[0:4:2])'''

#vowels

'''word="sanjana"
vowels="aeiou"
result=[char for char in word if char in vowels]
print(result)

#positive or negative
list=[int(x) for x in input().split()]
print(list)
print(type(list))'''

#set data type
'''friends={"sanjana",1,2,"siri"}
print(friends)
for i in friends:
    print(i)'''

#empty set
'''set3={}
print(type(set3))''' #treated as dictinoary

#set
'''states={"karnataka","tamil","maharastra"}
print(states)
for i in states:
    print(i)
states.add("andra")
print(states)'''

#set adding
'''district=set(["bellary","bng","koopal"])
print(district)
district.add("hubli")
print(district)'''

#removes duplicate
'''set1={10,20,30,40,40,20,50,90}
print(set1)
set1.add(120)
print(set1)'''

#update and add
'''set2={"sanjana","siri","addya"}
set2.update(["ramesh","vijaya"]);
print(set2)'''

'''set2=set(["sanjana","siri","uzma"])
set2.update(["ramesh","vijaya"])
print(set2)'''

#discard
'''set1={1,2,3,4,5}
print(set1)
set1.discard(1)
set1.remove(50)
print(set1)'''

#pop method
'''set1={1,2,3,4,5,6}
print(set1)
set1.pop()
set1.pop()
print(set1)
set1.clear()
print(set1)'''

#logical or in set
'''set1={"sun","mon","tue","wed"}
set2={"thur","fri","sat","sun","mon"}
print(set1-set2)
print(set2-set1)
print(set1^set2)
print(set1&set2) 
print(set1|set2) 
print(set1.union(set2)) #removes duplicate elements
print(set1.symmetric_difference(set2))'''

#nested list
'''matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)'''

#dictonar
'''details={"name":"sanjana","sem":3,"branch":"cse"}
print(details)
print(type(details))
dict={}
print(type(dict))
ldict = dict([(4, "sanjana"), (5, "siri")])
print(ldict)
'''
'''word = "balaji srinivasan"
vowels = "aeiou"
result1 = [char for char in word if char in vowels]
print(result1)
result2 = [char for char in word if char not in vowels]
print(result2)
j=0
word = "balajisrinivasan"

for i in range(len(word)-1):
    if(j==len(word)+1):
        break
    else:
        res = word[j] + word[j+1]+'-'
        j=j+3
        print(res,end="")'''
        
#exception handling
'''try:
    num=0
    deno=0
    result=num/demo
    print(result)
except:
    print("exception")
'''
#inbuilt keywords
'''try:
    list=[10,20,30]
    print(list[2]/0)
except ZeroDivisionError:
    print("denominator cannot be 0")
except IndexError:
    print("index out of bonds")'''

#even

'''try:
    num=int(input("enter a no'))
    assert num%2==0
except:
    print("not an even no")
else:
    reciprocal=1/num'''

filepath="file.txt"

filepath = "file.txt"
try:
    with open(filepath, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Closing the file")

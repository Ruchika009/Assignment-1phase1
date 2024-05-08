""" 

Problem: Knock Knock are you there?

Input Format:

1. Take M int input from the User 
2. Get M , seperated values from a user 
3. Enter a number 'N' you are looking for

Output Format:

1. Print index on console once Found or Print 'Better Luck Next Time' to the console


"""

ls=[]
M=int(input())
m=input("")    #Getting input from user having numbers seperated by,

value=''                      #Initializing value as a empty string
sum=0 

for i in range(len(m)):                  #using for loop to iterate from 0 to len(N)
    if m[i].isdigit() or m[i]=='-':      #using condition statement to check if string is integer or minus sign
        value+=m[i]                      #If above statement is true then add it to empty string named value
    
        
    elif m[i]==',':                          
#using another condition statement to check if semicolon is present or not if present then add numbers that are added in value string
                                            
        ls.append(int(value))    
         #adding values stored in value string also converting it from string to integer using int function
        value=''                  #after above steps storing value string empty to iterate for next char
    
ls.append(int(value))          #adding values in list named ls
#print(ls)

N=int(input()) 
count=0                #getting input from user to search for element in ls
for ele in ls:                 #using for loop for checking element is present in ls or not
    if N==ele:
        count+=1
#print(ele)
#print(count)
if count==1:
    print(ls.index(N,0,len(ls)))                  #prints index of element found using ls.index function
    
    
elif count==2:
    #print(ls.index(ele),end=' ')
    print(ls.index(ele,ls.index(N)+1,len(ls)+1))       #print index of element found if element is twice in list using index parameter of start and end
        
else:
    print("Better Luck Next Time")

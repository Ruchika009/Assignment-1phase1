"""
Problem 3: Reflection or Pratibimb 

Design and Develop a User Defined function named (reflection) pass the input literal 'Welcome to EN2004' and return Output Format Mentioned Below

Input Format:

1. Take M str input from the User 
2. Get M , seperated str literals from a user (Test string to pass: 'Welcome to EN2004')

Output Format:

EN2004
to
Welcome

"""
M=int(input())
m=input()                              #Taking input of string seperated by , from users
#i=0                                    #Initialize i=0
st=''                                 #Initialize str as empty string
ls=[]                                  #Initialize ls as empty list

for i in range(len(m)):                       #using for loop to iterate from 0 to length of str i.e M

    if (m[i].isalpha() or m[i].isdigit) and m[i]!=",":      
#using condition statement to check if str has char,digit and should not have comma

        st+=m[i]             #adding string to empty str if above condition statement is true
        #print(M[i])
    elif m[i]==',':           #if comma is present in string then add str in empty list named ls
        ls.append(st)
        
        st=''                #storing str as empty to store another string in list which is easier for iteration

ls.append(st)          #adding all strings which was broken into new string into this list named ls
#print(ls)

for ele in ls[::-1]:     
#using for loop to print string present in list in reverse order using ls[::-1],here -1 is gap between two elements in reverse order
    print(ele)
    

"""
Given a list of length M, you need to print and find sum of the elements of list 

Input Format :

Line 1 : An int M 
Line 2 : M int elements of list seperated by ';'

Output Format:

Addition 

Constraints :
1 <= M <= 10^6

"""
ls=[]                         #Taking empty list
M=int(input())                #Taking M number of integer in list
if(1 <= M <= 1000000):

    N=input("")                   #Getting M integers seperated by ; from user

    value=''                      #Initializing value as a empty string
    sum=0 
    #digit=0
    for i in range(len(N)):                  #using for loop to iterate from 0 to len(N)
        if N[i].isdigit() or N[i]=='-':      #using condition statement to check if string is integer or minus sign
            value+=N[i]                      #If above statement is true then add it to empty string named value


        elif N[i]==';':                          
    #using another condition statement to check if semicolon is present or not if present then add numbers that are added in value string

            ls.append(int(value))     #adding values stored in value string also converting it from string to integer using int function
            value=''                  #after above steps storing value string empty to iterate for next char

    ls.append(int(value))                 #storing numbers present in N to list named ls
    #print                              
    for ele in ls:                        #using for loop to add elements in list
        sum+=ele                          #adding all elements in list to sum which was initialially 0
    print(sum)                            #print sum

else:
    print()

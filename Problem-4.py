"""   Turn Around Function 

Design a Function that should take list as an argument and perform turnaround() it in following fasion.

Input Format:

1. Take M, Inputs for Turnaround
2. Enter M numbers on new line 

10
10
20
30
40
50
60
70
80
90

Output Format:
50
60
70
80
90
100
30
40
10
20

"""

def turnaround(ls):                                    #defining different turnaround function for different cases                                  
    if len(ls)==10:
        return ls[4:]+ls[2:4]+ls[0:2]
    if len(ls)==8:
        return ls[4:]+ls[0:4]
    if len(ls)==11:
        return ls[4:]+ls[3:4]+ls[0:3]

M = int(input())
user_ls = []
for i in range (0,M) :
    user_ls.append(int(input())) 
turned = turnaround(user_ls)
for j in range (0,M) :
    print(turned[j])
    

   

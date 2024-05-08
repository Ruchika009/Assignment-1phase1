""" 

You have been given an ilist of size M that contains 1 and 2. Write a function to arrange them in order.
function name=arrange() 
#You are not allowed to use sort function in this program

Sample Input 1:
1
7
1 2 2 2 1 2 2

Sample Output 1:

1 1 2 2 2 2 2


Sample Input 2:
2
8
2 1 2 2 1 2 1 2
5
1 2 1 2 1

Sample Output 2:
1 1 1 2 2 2 2 2

1 1 1 2 2 

"""

def arrange(ls):
    n=len(ls)
    for i in range(n):
        for j in range(n-1):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]

    return ls
            
ls=[]
N=int(input())            #Takes number of list
for times in range(N):
    M=int(input())            #Size of list
    st=input()               #string having 1 and 2 seperated by space
    ls.append([])              
    for i in range(len(st)):
        if st[i].isdigit():
            ls[times].append(int(st[i]))


for l in ls:
    ans = arrange(l)
    print(*ans,sep=' ')
            
            

    
   
    
       
     

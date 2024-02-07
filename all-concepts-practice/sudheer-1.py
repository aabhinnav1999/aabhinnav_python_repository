# num=int(input('enter the number of inputs:'))

# for i in range(0,num):
#     s=input('enter your inputs:')

s=[1,2,3,4,5]

for i in range(0,len(s)):
    for j in range(0,len(s)):
        if s[i]+s[j]==5:
            print(s[j],s[i])



    
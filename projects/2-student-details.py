count=0
class student:
    school_name='pyspiders'
    def __init__(self) -> None:
        self.name=self.uname(input("enter your name: "))
        self.phone=self.uphone(int(input("enter phone number please: ")))

    def uname(self,name):
        global count
        if count==2:
            print(name,"Not a Valid Name",end=' ')
            print("-----chances","3","of 3 completed-----")
            count=0
            return None
        if len(name)<3:
            print("name must contain 3 characters",end=' ')
            count+=1
            print("-----chances",count,"of 3 completed-----")

            res=self.uname(input("enter your name: "))
            return res
        elif not(('A'<=name[0]<='Z') or ('a'<=name[0]<='z')):
            print("first letter must be alphabet",end=' ')
            count+=1
            print("-----chances",count,"of 3 completed-----")
            res=self.uname(input("enter your name: "))
            return res
        else:
            for i in name:
                if not(('A'<=i<='Z') or ('a'<=i<='z')):
                    print("name should not contain",i,end=' ') 
                    count+=1
                    print("-----chances",count,"of 3 completed-----")   
                    res=self.uname(input("enter your name: "))
                    return res
            count=0
            return name.upper()
            
        
    def uphone(self,num):
        global count
        if count==2:
            print(num,"Not a Valid Number",end=' ')
            print("-----chances","3","of 3 completed-----")
            return None
        
        if len(str(num))==10:
            if str(num)[0] in '9876':
                return num
            else:
                print("number must start with 9 or 8 or 7 or 6",end=' ')
                count+=1
                print("-----chances",count,"of 3 completed-----")

                res=self.uphone(int(input("enter phone number: ")))
                return res
        elif len(str(num))<10:
            print("number must be 10 digits",end=' ')
            count+=1
            print("-----chances",count,"of 3 completed-----")

            res=self.uphone(int(input("enter phone number: ")))
            return res
        

     
obj=student()
            
print(obj.__dict__)
        

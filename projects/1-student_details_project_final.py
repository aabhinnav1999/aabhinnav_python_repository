class student:
    c_name='pyspiders'

    def __init__(self,name,m_no,email_id,branch,password,re_password):
        self.name=self.nupper(name)
        self.m_no=self.check(m_no)
        self.email_id=self.email(email_id)
        self.branch=self.bupper(branch)
        self.password=self.checkpassword(self.upassword(password),re_password)

    @staticmethod
    def nupper(coll):
        st=''
        for i in coll:
            if 'a'<=i<='z':
                st+=chr(ord(i)-32)
            else:
                st+=i
        return st

    @staticmethod
    def check(coll):
        if len(str(coll))==10:
            if str(coll)[0]=='9' or str(coll)[0]=='8' or str(coll)[0]=='7' or str(coll)[0]=='6':
                return coll
                
            else:
                print('number must start with 9 or 8 or 7 or 6')
                v=student.check(int(input('enter number:')))
                return v
        else:
            print('number should be 10 digits')
            v=student.check(int(input('enter number:')))
            return v
            

    def email(self,coll):
        if len(coll)>10:
            if self.mycount(coll,'.')>=1 and self.mycount(coll,'@')==1:
                return coll
            else:
                print('enter correct email')
                v=self.email(input('again enter emailid:'))
                return v
        else:
            print('email must be more than 10 characters')
            v=self.email(input('again enter emailid:'))
            return v


    @staticmethod
    def bupper(coll):
        st=''
        for i in coll:
            if 'a'<=i<='z':
                st+=chr(ord(i)-32)
            else:
                st+=i
        return st


    def checkpassword(self,coll1,coll2):
        if coll1==coll2:
            return coll1
        else:
            res=self.checkpassword(coll1,input('re-enter your password:'))
            return res

    def upassword(self,coll):
        if len(coll)>=5:
            if 'A'<=coll[0]<='Z':
                countnum=0
                for i in coll:
                    if '0'<=i<='9':
                        countnum+=1
                        
                if countnum>=1:
                    countsp=0
                    for i in coll:
                        if not (('a'<=i<='z') or ('A'<=i<='Z') or ('0'<=i<='9')):
                            countsp+=1
                            
                    if countsp>=1:
                        return coll
                    
                    else:
                        print('password must contain atleast one special character')
                        v=self.upassword(input('again enter password:'))
                        return v
                        
                else:
                    print('password must contain atleast one numeric')
                    v=self.upassword(input('again enter password:'))
                    return v
                        
                
            else:
                print('password must start with uppercase character')
                v=self.upassword(input('again enter password:'))
                return v

        else:
            print('password should contain atleast five characters')
            v=self.upassword(input('again enter password:'))
            return v

    def studentdetails(self,count=0):
        a=input('enter email_id for details:')
        b=input('enter password for details:')
        
            
        if count==3:
            print('exceeded your re-enter password attemts')
            return
        if a==self.email_id:
            if b==self.password:
                print('college name:',self.c_name)
                for i in self.__dict__:
                    if self.__dict__[i]!=self.password:
                        print(i,':',self.__dict__[i])
            else:
                print('password is wrong')
                self.studetails(count+1)
        else:
            print('email_id is wrong')
            self.studetails(count+1)


    
    def mycount(self,coll,st,count=0):
        for i in coll:
            if i ==st:
                count+=1
        return count
        
        
        

#stud1=student("gopi",9100584972,input('enter email:'),'cse',input('enter password:'),input('re-enter your password:'))
    
stud1=student(input('enter name:'),int(input('enter mobile number:')),input('enter email_id:'),input('enter branch:'),input('enter password:'),input('re-enter your password:'))




                            
                    
                
            
            
        





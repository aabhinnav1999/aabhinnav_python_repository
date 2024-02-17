class bank:
    bank_name="HDFC"
    bank_location="HYDERABAD"

    def __init__(self,name) -> None:
        import datetime,csv
        d=datetime.datetime.now()
        self.name=name
        self.created_on=d.date()
        self.account_no=str(d.timestamp()).split('.')[0]
        self.balance="{:.2f}".format(0.00)
        fo=open(r"D:\Python\all-concepts-practice\9-1.csv",'a',newline='')
        fa=csv.writer(fo)
        fa.writerow([self.account_no,self.name,self.created_on,int(self.balance)])
        fo.close()

def add(name,money):
    import csv
    fo=open(r"D:\Python\all-concepts-practice\9-1.csv",'r')
    fr=csv.reader(fo)
    res=[]
    for i in fr:
        res+=[i]

    for i in res:
        if i[1]==name:
            print(i)
            i[-1]="{:.2f}".format(money)
            print(i)
    fo=open(r"D:\Python\all-concepts-practice\9-1.csv",'w',newline='')
    fw=csv.writer(fo)
    fw.writerows(res)
    fo.close()


# customer=bank(input("enter customer name: "))
    
print(add('pavan',1225))


        


    
    


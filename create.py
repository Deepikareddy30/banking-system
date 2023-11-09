import mysql.connector

#creating connection

class insert:
    def __init__ (self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Akki@kutty25",
                database = "banking"
                )


# create  cursor-- (for executing queries)
    def personal_details(self,cid,fname,lname,addr,pn,an,pan):
        cur = self.conn.cursor() # creating cursor
        cur.execute(f"insert into personal_details values({cid},'{fname}','{lname}','{addr}',{pn},{an},'{pan}')")
        self.conn.commit()
        print("-----------------personal information has been saved sucessfully------------------:")

    def bank_details(self,acn,cid,ifsc,actype):
        cur = self.conn.cursor()
        cur.execute(f"insert into bank_details values({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("----------------bank information has been sucessfully saved---------------------:")
    
    def transaction_details(self,transid,sacn,racn,amount,mth):
        cur = self.conn.cursor()
        cur.execute(f"insert into transaction_details values({transid},{sacn},{racn},{amount},'{mth}')")
        self.conn.commit()
        print("------------------transaction information has been sucessfully saved---------------------:")
    
    def account_details(self,acn,transid,amount,cbalance,tp):
        cur = self.conn.cursor()
        cur.execute(f"insert into account_details values({acn},{transid},{amount},{cbalance},'{tp}')")
        self.conn.commit()
        print("---------------account information has been saved sucessfully----------------:")
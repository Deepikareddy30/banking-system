import mysql.connector

class read:
    def __init__ (self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Akki@kutty25",
                database = "banking"
                )
        
    def specific_info(self,customer_id,table_name):
        cur = self.conn.cursor()
        if table_name =='personal_details' or table_name=='bank_details':
            cur.execute(f"select * from {table_name} where customerid={customer_id}")
            print(cur.fetchall())
        
        if table_name=='transaction_details':
            cur.execute(f'''select * from transaction_details where transactionid in
                        (select transactionid from account_details where account_number in
                        (select account_number from bank_details where customerid ={customer_id}));
                        ''')
            print(cur.fetchall())
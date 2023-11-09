import mysql.connector

#creating connection

class update:
    def __init__ (self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Akki@kutty25",
                database = "banking"
                )

    def myupdate(self,table_name,column_name,new_value,cusid):
        cur = self.conn.cursor()
        if new_value.isnumeric():
            print("test1")
            cur.execute(f"update {table_name} set {column_name}={int(new_value)} where customerid={cusid}")
        else:
            print("test2")
            cur.execute(f"update {table_name} set {column_name}='{new_value}' where customerid={cusid}")
        self.conn.commit()
        print("updated sucessfully")
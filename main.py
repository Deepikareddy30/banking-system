from create import insert
from read import read
from update import update
from delete import delete

obj = insert()
objread = read()
objupdate = update()
objdelete = delete()

print("-------------- bank management system --------------------")
print("for inserting the data press 1 :")
print("for reading the data press 2 :")
print("for updating the data press 3 :")
print("for deleting the data press 4 :")

opr = int(input("enter your opreation:"))

def myopr():
    print("--------- for perosnal information press 1 -------")
    print("--------- for bank details press 2 -------")
    print("--------- for transaction detailspress 3 -------")
    print("--------- for account details press 4 -------")
    vr = int(input("please select your table:"))
    if vr == 1:
        return 'personal_details'
    elif vr == 2:
        return 'bank_details'
    elif vr == 3:
        return 'transaction_details'
    elif vr ==4:
        return 'account_details'
    

if opr ==1:
    h = myopr()  # h 'account_details'
    if h =='personal_details':
        cid = int(input("please enter customer id:"))
        fname = input("please enter customer first name:")
        lname = input("please enter customer last name:")
        addr = input("please eneter customer address:")
        pn = int(input("please enter customer phone number:"))
        an = input("please enter customer aadhar number:")
        pan = input("please enter customer pan number:")
        obj.personal_details(cid,fname,lname,addr,pn,an,pan)
    elif h=='bank_details':
        acn = int(input("enter account number:"))
        cid = int(input("enter customer number:"))
        ifsc = input("enter ifsc code :")
        actype = input("enter account type:")
        obj.bank_details(acn,cid,ifsc,actype)
    elif h=='transaction_details':
        transid = int(input("enter transaction id:"))
        sacn = int(input("enter sender_account:"))
        racn = int(input("enter reciever_account:"))
        amount = int(input("enter amount:"))
        mth = input("enter method:")
        obj.transaction_details(transid,sacn,racn,amount,mth)
    elif h=='account_details':
        acn = int(input("enter account number:"))
        transid = int(input("enter transaction id:"))
        amount = int(input("enter amount:"))
        cbalance = int(input("enter balance:"))
        tp =input("enter transaction type")
        obj.account_details(acn,transid,amount,cbalance,tp)

if opr == 2:  # user wanted to read the data
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    objread.specific_info(cusid,j)
    
if opr ==3:
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    colname = input("please enter column name:")
    newval = input("please enter new values:") # 500 str # 'jhon'
    objupdate.myupdate(j,colname,newval,cusid)

if opr ==4:
    k = myopr()
    cusid = int(input("enter customer id to delete the data:"))
    objdelete.specific_del(k,cusid)
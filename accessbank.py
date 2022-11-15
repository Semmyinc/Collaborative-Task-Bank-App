import mysql.connector
connect = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='verification')
manage = connect.cursor()
import re
import random
press = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# PHONE NUMBER VERIFICATION  AND NETWORK IDENTIFIER METHOD USING LIST METHOD( NO ERROR)
mtn = ['0803','0806','0814','0810','0813','0814','0816','0703','0706','0903','0906','+234803','+234806','+234814','+234810','+234813','+234814','+234816','+234703','+234706','+234903','+234906']

# PHONE NUMBER VERIFICATION AND NETWORK IDENTIFIER PROVEN NOT ACCURATE
mwork = r'(^0[7|8|9]{1}[0|1]{1}[0-9]{8})|(^\+234{1}[7|8|9]{1}[0|1]{1}[0|1|3|4|6]{1}[0-9]{7})'

# mwork = r'\d{0803}\d{0806}\d{0814}\d{0813}\d{0816}\d{0703}\d{0706}\d{0903}\d{0906}\d{0904}'


# mwork = r'\d{0803}\d{0806}\d{0814}\d{0813}\d{0816}\d{0703}\d{0706}\d{0903}\d{0906}\d{0904}'




# ((^0)(7|8|9{1}()))

# ((^0)(7|8|9){1}(0|1){1}[0–9]{8}))
# this expressions matches:

# (^0) any text that begins with a “0”, followed by

# (7|8|9){1} exactly one occurrence of any of the text “7”, “8” or “9”, followed by

# (0|1){1} exactly one occurrence of any of the text “0” or “1”, followed by

# [0–9]{8} eight occurrences of any digit from 0 to 9.

# The regular expression we have discussed, will validate Nigerian phone numbers from the popular carriers in whatever form they are written.


# # CREATE DATABASE
# manage.execute("CREATE DATABASE verification")
# manage.execute("SHOW DATABASES")
# for db in manage:
#     print(db)
# MTN = [0803,0806,0814,0810,0813,0814,0816,0703,0706,0903,0906]

# CREATE TABLE
# manage.execute("CREATE TABLE newdata (Mobile_Number varchar(11), BVN INT(12))")
# manage.execute("SHOW TABLES")
# for table in manage:
#     print(table)

# manage.execute("ALTER TABLE accessbank add column total_balance INT (10) NOT NULL")
# manage.execute("SHOW TABLES")
# for table in manage:
#     print(table)
# ALTER TABLE
# manage.execute("ALTER TABLE newdata add Service_Oper VARCHAR (12) NOT NULL")
# manage.execute("SHOW TABLES")
# for table in manage:
#     print(table)

class Verify:
    
    def __init__(self):
        self.vn= 'vn'

    def bvn(self):
        phone = input("Enter your Mobile Number>>>>:")
        if phone[:4] in mtn and len(phone)==11 or phone[:7] in mtn and len(phone)==14:
        # if(re.search(mwork, self.Mobile_Number)):
            print("MTN")
        else:
            print("Invalid Phone Number")
            # BVN GENERATOR VALIDAATE AND GOES INTO DATABASE
        self.bvn = random.randrange(222222222222, 222222222852)
        bank_customer = 'INSERT into newdata (Mobile_Number, Bvn) VALUES(%s,%s)'
        details = (phone, self.bvn)
        manage.execute(bank_customer, details)
        connect.commit()
        print(manage.rowcount, 'record(s) inserted successfully')
        print(f'You have signed up successfully')
        print(f'Your BVN is {self.bvn}!')

    def confirm(self):
        self.bvn = input("Enter your BVN for Verification>>>>:")
        check = input("confirm your BVN for Verification>>>>:")
        if check == self.bvn:
            print("Your BVN has been successfully verified!")
        else:
            print("Wrong BVN,Please recheck and try later!")
            quit()


var = Verify()
var.bvn()
var.confirm()

# phone = input("Enter your phone number")
# if phone(:4) in mtn and len(phone)==11 or phone(:7) in mtn and len(phone)==13:
#     print("MTN")



# MTN = [0803,0806,0814,0810,0813,0814,0816,0703,0706,0903,0906]
# phone = input("Enter your Phone Number")
# if re.search("\d{0}\d{7}\d{0}\d{3},\d{0}\d{7}\d{0}\d{6},\d{0}\d{8}\d{0}\d{3},\d{0}\d{8}\d{0}\d{6},\d{0}\d{8}\d{1}\d{0}\d{0}\d{8}\d{1}\d{3},\d{0}\d{8}\d{1}\d{4},\d{0}\d{8}\d{1}\d{6},\d{0}\d{9}\d{0}\d{3},\d{0}\d{9}\d{0}\d{6},\d{0}\d{9}\d{1}\d{3} ," phone ):
#     print(MTN)
# glo = [0805,0807, 0705, 0815, 0811, 0905]
# Airtel = [0802, 0808, 0812,0701,0708,0902,0907,0901]
# ninemobile = [0809,0817,0818,0908,0909]
# phone = input("Enter your mobile number")




    # def customer_signup(self):
        # print(f'Welcome to Access Bank,Please sign up to enjoy our services')
        # self.firstname = input('Enter your Firstname>>>:')
        # self.surname = input('Enter your Surname>>>:')
        # self.email = input('Enter your email>>>:')
        # if(re.fullmatch(press, self.email)):
        #     print('Email Valid')
        # else:
        #     print("Please Enter a valid Email")
        #     quit()
        # self.password = input('Password>>:')
        # self.con_password = input('Confirm Password')
        # if self.con_password != self.password:
        #     print('Password not the same')
        #     quit()
        # else:
        #     print('Password Verified!')
        # self.bvn = int(input('Enter your BVN'))
        # self.username = input('Enter your username')
        # self.pin = int(input('Enter your pin'))
        # self.confirm_pin = int(input('Confirm your Pin'))
        # if self.pin == self.confirm_pin:
        #     print(f'Welcome {self.firstname}!\n Enjoy Banking with us!')
        # else:
        #     print('Pin not Verified!')
        #     quit()
        # bank_customer = 'INSERT into accessbank (Firstname, Surname, Email, Password, bvn, Username, Pin, Account_number, Deposit, Withdrawal, Account_Balance) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # details = (self.firstname, self.surname, self.email, self.password, self.bvn, self.username, self.pin, 0, 0, 0, 0)
        # manage.execute(bank_customer, details)
        # connect.commit()
        # print(manage.rowcount, 'record(s) inserted successfully')
import testData
from testData import *
import creds
from creds import sqluser
from creds import sqlpass
import time
import mysql.connector


# starting the connection to the mysql server
cnx = mysql.connector.connect(user = 'root',
                              password = '********',
                              host = '127.0.0.1',
                              database = 'customerinfo')
cursor = cnx.cursor()


# the purpose of the terminaltest function is to verify that the data being printed to the terminal can
# be used to verify the correct info was placed into the mysql database docs will be exp in unit testing
#while also generating the data and storing it to lists for easy manipulation
terminalTest()


# bringing in my variables from testdata, since we want the same instance of random data being shown in the test
# to be entered into the databases , remember we are not creating tables we are inserting into existing tables and db
# we are also going to be printing these during dev to make sure im getting the values from testdata correctly
airline_name = testData.airline_name
airline_codes = testData.airline_codes
credit_score = testData.credit_score
routing_number = testData.routing_number
credit_card_number = testData.credit_card_number
card_provider = testData.card_provider
card_security_code = testData.security_code
customer_name = testData.cust_name
customer_city = testData.cust_city
customer_address = testData.cust_address
customer_job = testData.cust_job
print(airline_codes)
print(airline_name)
print(credit_score)
print(routing_number)
print(credit_card_number)
print(card_provider)
print(card_security_code)
print(customer_name)
print(customer_city)
print(customer_address)
print(customer_job)


# we have tested all of the above variables and they are good
# we want to split the items up into lists as opposed to dicts and tuples since we want to allow for the
# potential of duplicates in the data sets and will make it easier to throw the into various database tables


#to execute anything in mysql through the python connector we will need to store the sql query into a variable
#and then use the cursor method to execute those queries



# ====================================

update_flight = ("""
INSERT INTO flightinfo(airline_name, airline_code) VALUES (%s,%s)
""")
update_custinfo = ("""
INSERT INTO customer_info(customer_address, customer_job) VALUES(%s,%s)
""")
update_custname = ("""
INSERT INTO customer_names(customer_name, customer_city) VALUES(%s,%s)
""")
update_payment = ("""
INSERT INTO payment_account(account_number, security_code) VALUES(%s,%s)
""")
update_paymentcard = ("""
INSERT INTO payment_card(card_number, card_provider, credit_score) 
VALUES (%s, %s, %s)
""")


for name, code in zip(airline_name, airline_codes):
    flightinfo_data = (str(name), str(code))
    cursor.execute(update_flight, flightinfo_data)


for number, provider, score in zip(credit_card_number, card_provider, credit_score):
    card_info = (str(number), str(provider), int(score))
    cursor.execute(update_paymentcard, card_info)


for name, city in zip(customer_name, customer_city):
    customer_personal = (str(name), str(city))
    cursor.execute(update_custname, customer_personal)

for account, code in zip(routing_number, security_code):
    account_info = (str(account), str(code))
    cursor.execute(update_payment, account_info)



for address, job in zip(customer_address, customer_job):
    customer_info = (str(address), str(job))
    cursor.execute(update_custinfo, customer_info)



# ====================================


cnx.commit()
cursor.close()
cnx.close()

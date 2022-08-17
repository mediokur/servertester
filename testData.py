from faker import Faker
import time
import json
from faker_credit_score import CreditScore
from faker_airtravel import AirTravelProvider


# instantiate the faker class objects for airline info and credit card info since they arent standard faker objects
fake = Faker()
fake.add_provider(CreditScore)
fake.add_provider(AirTravelProvider)


# this cli argument will allow me to run the test multiple times manually with a change of value for each run
# since the records value will control the amount of fake information being produced and stored for each run
print("How many records do you want produced for this test?\n")
records = int(input())


# terminaltest will be the function that calls all of the functions that both create our variables to use in the db
# and also prints our values to the terminal for verification
def terminalTest():
    fakeFlight()
    fakeCode()
    fakeScore()
    fakeRoutingNumber()
    fakeCreditNumber()
    fakeCreditProvider()
    fakeCardSecurity()
    fakeName()
    fakeCity()
    fakeAddress()
    fakeJob()


# this is where we are going to instantiate the lists that will be amended in the functions for their storing their
# json data as python string or int data, they will be brought as list variables into main
airline_name = []
airline_codes = []
credit_score = []
routing_number = []
credit_card_number = []
card_provider = []
security_code = []
cust_name = []
cust_city = []
cust_address = []
cust_job = []


def fakeFlight():
    count = 0
    while count in range(records):
        airlines = str(fake.airline())
        airline = airlines.split()[:-1]   #--this slice ensures we get rid of the word airline for every airline
        airline_name.append(airline)
        time.sleep(.5)

        count += 1
    # print(airline_name) --dont need this anymore moving the print for testing over to main


def fakeCode():
    count = 0
    while count in range(records):
        codes = str(fake.airport_icao())
        airline_codes.append(codes)
        time.sleep(.5)
        count += 1
    # print(airline_codes) --dont need this anymore moving the print for testing over to main and rest of functions
    # will now be print tested in main


def fakeScore():
    count = 0
    while count in range(records):
        score = int(fake.credit_score())
        credit_score.append(score)
        time.sleep(.5)
        count +=1


def fakeRoutingNumber():
    count = 0
    while count in range(records):
        routing = str(fake.aba())
        routing_number.append(routing)
        time.sleep(.5)
        count +=1


def fakeCreditNumber():
    count = 0
    while count in range(records):
        number = str(fake.credit_card_number())
        credit_card_number.append(number)
        time.sleep(.5)
        count +=1


def fakeCreditProvider():
    count = 0
    while count in range(records):
        provider = str(fake.credit_card_provider())
        card_provider.append(provider)
        time.sleep(.5)
        count +=1


def fakeCardSecurity():
    count = 0
    while count in range(records):
        security = str(fake.credit_card_security_code())
        security_code.append(security)
        time.sleep(.5)
        count +=1


def fakeName():
    count = 0
    while count in range(records):
        fakename = str(fake.name())
        cust_name.append(fakename)
        time.sleep(.5)
        count +=1


def fakeCity():
    count = 0
    while count in range(records):
        fakecity = str(fake.city())
        cust_city.append(fakecity)
        time.sleep(.5)
        count += 1


def fakeAddress():
    count = 0
    while count in range(records):
        fakeaddress = str(fake.address())
        cust_address.append(fakeaddress)
        time.sleep(.5)
        count += 1


def fakeJob():
    count = 0
    while count in range(records):
        fakejob = str(fake.job())
        cust_job.append(fakejob)
        time.sleep(.5)
        count +=1
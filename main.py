import os
from pymongo import MongoClient
from gs_functions import *
from ftplib import FTP
from dataclasses import dataclass
import logging
import json
import sys


def stop():
    # press_any_key()
    sys.exit("\n********************\nGS - program stopped by stop() functions")


def press_any_key():
    # input('press enter to end of program')
    print('\n')
    os.system('pause')
    print('Bye')


@dataclass
class Person:
    name: str
    job: str
    age: int
    spouse: str

    def __str__(self):
        return (f'{self.name} {self.job} age:{self.age} spouse: {self.spouse}')


dict1 = {
    'Name': 'Geeks',
    'Name2': 'Geeks',
    'list': ['item 1', 'item 2', 'item 3', 'item 4']
}
print("\nDictionary:")
print(dict1)

json_object = json.dumps(dict1, indent=4)
print("\nDictionary converted to json:")
print(json_object)

# stop()

# classes & dataclass module
print('\nclasses & dataclass module')

person1 = Person('gal sarig', 'CEO', 54, 'sigal')
person2 = Person(job='CEO', spouse='sigal', age=54, name='gal sarig')
# print(person1.name)
print(vars(person1))
print(person1)


def print_hi(name2):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi {name2},\nYour name is coming from a dictionary')  # Press Ctrl+F8 to toggle the breakpoint.


name = {
    "first": "Gal",
    "last": "Sarig",
    "middle": "GS"
}

print_hi(name['first'])
print(f'Python version {get_python_version()}')
print(f'script name: {__name__}')
print(f'file name: {__file__}')

# PyMongo tutorial: https://pymongo.readthedocs.io/en/stable/tutorial.html
print('\nMongoDB')
db = open_mongodb_connection()

new_db_doc = {
    "name": {
        'first': 'New',
        'last': 'Name',
    },
    'initials': 'NN',
    'age': 54,
    'pics': ['location1', 'location2', 'location 3']
}

db.insert_one(new_db_doc)
print('new document added to DB')

filter_json = {
    'name.last': 'Sarig',
    "name.first": {
        "$regex": '.*a.*',  # includes
        "$options": 'i'  # case insensitive
    }
}
# 'name.first' : {$regex: /.*a.*/},
# 'name.first': {
#     '$regex': '/.*a.*/'
# }
# regex - contains 'a' ????? REGEX NOT WORKING ??????
# $options" :'i'
# case-insensitive

sort_by = [('name.first', 1)]

results = db.find(
    filter=filter_json,
    sort=sort_by
)

print("\nMongoDB query results:")

result_number = 0
for record in results:
    result_number += 1
    results_items = record['name']
    print(str(result_number) + ' ' + results_items['first'] + ' ' + results_items['last'])

if result_number == 0:
    print('No matching results')


# Higher order functions
def divisor(x):
    def dividend(y):
        return y / x

    return dividend


divide = divisor(2)
print(f'\nHigher order functions\ndivide: {divide(10)}')

# decorators & wrappers
print('\nDecorators & Wrappers')


def decorator(original_func):  # the outer function that gets a function as parameter
    def wrapper():  # inner function that uses the original function but wraps it
        print('im running before')  # work before running
        original_func()  # original function execution
        print('im running after')  # work after running

    return wrapper


@decorator
def do_stuff():
    print('I do stuff')


do_stuff()


# Instead of "@" we can do:
# decorated = decorator(do_stuff)
# decorated()


def decorator2(original_func):  # the outer function that gets a function as parameter
    def wrapper2(*args, **kwargs):  # inner function that uses the original function but wraps it
        print('\nI\'m running before')  # work before running
        original_func(*args, **kwargs)  # original function execution
        print('I\'m running after')  # work after running

    return wrapper2  # return edited function


@decorator2
def do_stuff2(stuff, more_stuff):
    print(f'I do {stuff} and {more_stuff}')


do_stuff2('work', 'even more work')

# create a file in a local folder (PC)
s = sys.platform
print('operation system: ' + s)
if s == "linux" or s == "linux2":
    # print('linux')
    do_nothing()
elif s == "darwin":
    # print('OS X')
    f = open("/Users/galsarig/Downloads/tst.txt", 'w')
    f.write("Hello. I've created a file")  # writing to file
    f = open('/Users/galsarig/Downloads/tst.txt', 'r')
    print(f.read())
    f.close()
elif s == "win32":
    f = open("c:/tmp/tst.txt", 'w')
    f.write("Hello. I've created a file")  # writing to file
    f = open('C:/tmp/tst.txt', 'r')
    print(f.read())
    f.close()


def logger_add_and_dosplay():
    loggerfilename = 'testlogger.log'
    if os.path.exists(loggerfilename):
        os.remove(loggerfilename)
    logging.basicConfig(filename=loggerfilename, encoding='utf-8', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
    print('\nDisplay logger file')
    f = open(loggerfilename, 'r')
    print(f.read())
    f.close()


logger_add_and_dosplay()

print('\nFTP')

ftp = FTP('ftp.galsarig.com')  # connect to host, default port
ftp.login('latingate', 'ggal5313Y!')  # user anonymous, passwd anonymous@
ftp.cwd('ftp_test')

# hellmann's robot ftp (internal IP)
# ftp = FTP('172.20.2.142')  # connect to host, default port
# ftp.login('gal', 'nhfk7@G')  # user anonymous, passwd anonymous@
# ftp.cwd('/robot')

file_to_be_uploaded = open('tst.txt', 'rb')
# for line in file_to_be_uploaded:
#     print(line)
ftp.storbinary('STOR uploaded_testfile.txt', file_to_be_uploaded)

file_downloaded = open('tst_downloaded.txt', "wb")
ftp.retrbinary('RETR uploaded_testfile.txt', file_downloaded.write)

# ftp.retrlines('LIST')  # list directory contents  # print  directory contents
ftp.dir()
print('current directory: ' + ftp.pwd())
ftp.close()

# ftp.quit()

while True:
    try:
        x = int(input('enter a number: '))
        y = int(x / 0)
        # break
    except ValueError as err:
        print("Oops!  That was no valid number.  Try again...", err)
        print(ValueError)
    # except ZeroDivisionError:
    #     print("divided by zero")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        # raise


# press_any_key()

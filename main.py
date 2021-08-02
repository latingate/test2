import os
from pymongo import MongoClient
from gs_functions import *
from ftplib import FTP
import logging

def print_hi(name2):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi {name2},\nThis is your first Python program')  # Press Ctrl+F8 to toggle the breakpoint.


name = {
    "first": "Gal",
    "last": "Sarig",
    "middle": "GS"
}

print_hi(name['first'])
print(f'Python version {get_python_version()}')
print(f'script name: {__name__}')
print(f'file name: {__file__}')

db = open_mongodb_connection()

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


# classes & dataclass module
print('\nclasses & dataclass module')


class Person:
    name: str
    job: str
    age: int

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age


person1 = Person('gal sarig', 'CEO', 54)
print(person1.name)


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

print('\nCreate a file in a local folder')
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
# ftp.retrlines('LIST')  # list directory contents  # print  directory contents
ftp.cwd('ftp_test')
ftp.dir()
print('current directory: ' + ftp.pwd())
ftp.close()


# ftp.quit()


def press_any_key():
    # input('press enter to end of program')
    print('\n')
    os.system('pause')
    print('Bye')

# press_any_key()

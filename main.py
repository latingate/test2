from gs_functions import *
from pymongo import MongoClient

import gs_functions


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
    # 'name.first' : {$regex: /.*a.*/},
    # 'name.first': {
    #     '$regex': '/.*a.*/'
    # }
    # regex - contains 'a' ????? REGEX NOT WORKING ??????
    # $options" :'i'
    # case-insensitive
}

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

print(f'current date: {current_date_dd_mm_yyyy()}')
print(f'current time: {current_time()}')
date_object = str_to_date_object("9.5.1967")
print(date_object)

print('End of program')

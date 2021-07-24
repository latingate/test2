# Gal Sarig's Functions

# System Functions
# ================
import sys
from pymongo import MongoClient


def check_python_version():
    s = sys.version_info
    version = str(s[0]) + '.' + str(s[1]) + '.' + str(s[2])
    return version


def open_mongodb_connection():
    conn = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
    db = conn['tstdb']['tst2']
    return db

# User Functions
# ================




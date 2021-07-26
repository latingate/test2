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

    # conn = MongoClient('mongodb+srv://latingate:mgal5313b@cluster0.oss2v.mongodb.net/gal-tst-db?authSource=admin&replicaSet=atlas-wgu8qa-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
    # db = conn['gal-tst-db']['gal-tst-1']

    return db

# User Functions
# ================

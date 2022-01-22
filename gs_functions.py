# Gal Sarig's Functions

import sys
import os
import time
from pathlib import Path
from pymongo import MongoClient
import hashlib, binascii
import base64
import configparser


# System Functions
# ================


def get_python_version():
    s = sys.version_info
    version = str(s[0]) + '.' + str(s[1]) + '.' + str(s[2])
    return version


def get_path(file='.'):
    # return os.path.dirname(__file__)
    try:
        if Path(file).exists():
            return Path(file).resolve()
        else:
            print('*err - Path does not exists')
            return ''
    except:
        return False


def open_mongodb_connection():
    # local
    # conn = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
    # db = conn['tstdb']['tst2']
    conn = MongoClient(
        f'mongodb://{config["mongoDB"]["host"]}:{config["mongoDB"]["port"]}/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
    db = conn[config['mongoDB']['database']][config['mongoDB']['collection']]

    # cloud (MongoDB Atlas)
    # conn = MongoClient("mongodb+srv://latingate:mgal5313b@cluster0.oss2v.mongodb.net/gal-tst-db?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
    # db = conn['gal-tst-db']['gal-tst-1']

    return db


def current_time():
    local_time = time.localtime()
    return time.strftime("%H:%M", local_time)


def current_date_dd_mm_yyyy():
    local_time = time.localtime()
    return time.strftime("%d.%m.%Y", local_time)


def str_to_date_object(string):
    # dd.mm.yyyy
    return time.strptime(string, "%d.%m.%Y")


# User Functions
# ================


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    # print(f'salt: {salt}')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def encrypt_string(string, key):
    string_plus_key = key + string
    string_to_encode = string_plus_key.encode("utf-8")
    return base64.b64encode(string_to_encode)


def decrypt_tring(string, key):
    decrypted_string = base64.b64decode(string)[len(key):]
    return decrypted_string


def none2empty(s):
    if s == None:
        return ''
    else:
        return s


# read config file
# ================

config = configparser.ConfigParser()
config_file = 'gs_config.ini'
# config.read('gs_config.ini')
# config.read(os.path.join(os.path.dirname(__file__), 'gs_config.ini'))
config.read(get_path(config_file))
# print(config['mongoDB']['host'])
# print(config.sections())

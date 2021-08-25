import mongoengine


def mongoengine_connect():
    mongoengine.register_connection(alias='alias_db', name='tstdb', host='localhost', port=27017)


mongoengine_connect()


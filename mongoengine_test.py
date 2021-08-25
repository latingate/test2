import mongoengine


def mongoengine_connect():
    mongoengine.register_connection(alias='alias_db', name='tstdb')


mongoengine_connect()


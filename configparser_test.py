import configparser

config = configparser.ConfigParser()

# write to config file (deletes previous data)

config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'gal'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'

with open('configparser_test.ini', 'w') as configfile:
    config.write(configfile)



# read from config file

config = configparser.ConfigParser()

config.read('configparser_test.ini')
print(config.sections())
print('bitbucket.org' in config)
print('bytebong.com' in config)
print(config['bitbucket.org']['User'])
print(config['DEFAULT']['Compression'])
topsecret = config['topsecret.server.com']
print(topsecret['Port'])
for key in config['bitbucket.org']:
    print(key)
print(config['bitbucket.org']['ForwardX11'])

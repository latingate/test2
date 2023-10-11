import re

# Sigal - check cellular phone prefix

def tst1(s) :
    if s.startswith('05'):
        return 'ok'
    else:
        return 'not ok'

def tst2(s) :
    match s.startswith('05'):
        case True:
            return 'ok'
        case False:
            return 'not ok'


def tst3(s):
    if not s.startswith('05'):
        return 'not ok'
        # return HttpResponse(status_code=400, body=json.dumps("Error: Invalid mobile number"), headers={'Content-Type': 'application/json'})

def tst4(s):
    # https://regexr.com/
    reExpr = '^(\+?(972)|0)(\-)?([5]{1}\d{8})$'
    r = re.fullmatch(reExpr, s)
    if not r:
        return 'this is not a valid cellphone number'
    else:
        return 'valid phone number'

phoneNumber = '972547007770'
print (phoneNumber)
print ('tst1', tst1(phoneNumber))
print ('tst2', tst2(phoneNumber))
print ('tst3', tst3(phoneNumber))
print ('tst4', tst4(phoneNumber))

reExpr = '^(\+?(972)|0)(\-)?([5]{1}\d{8})$'
r = re.fullmatch(reExpr, phoneNumber)
if not r:
    print('not good number')

# import http.client
# conn = http.client.HTTPConnection('uppersite.com')
# gs = http.client.HTTPResponse
# print(gs)
# attrs = vars(gs)
# for key,value in attrs.items():
#     print (str(key) + ' value= ' +str(value))
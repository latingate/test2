import spf

print(spf.check(i='103.47.205.84', s='gal2016@latingate.com', h='smtp2go.com'))
print(spf.check(i='103.47.205.84', s='gal2016@latingate.com', h='XXXXXsmtp2go.comXX'))
print(spf.check(i='103.47.205.84', s='gal2016@latingate.com', h=''))
print(spf.check(i='0.47.205.84', s='gal2016@latingate.com', h=''))

print(spf.check(i='104.47.14.56', s='gals@hellmann.co.il', h='hellmann.co.il'))
print(spf.check(i='0.47.14.56', s='gals@hellmann.co.il', h='hellmann.co.il'))
print(spf.check2(i='0.47.14.56', s='gals@hellmann.co.il', h='hellmann.co.il'))

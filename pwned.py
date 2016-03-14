import sys, json, urllib2

link = 'https://haveibeenpwned.com/api/v2/breachedaccount/%s' % raw_input('Enter your email: ')

try:
    response = urllib2.urlopen(link)
    data = response.read()
    
except Exception:
    sys.exit('You were not pwned. You are safe :)')

pwns = json.loads(data)
print 'you were pwned at the following breaches:\n'

count = 1
for pwn in pwns:
    print '%2d) %-40s %s' %(count, pwn['Name'], pwn['Domain'])
    count += 1

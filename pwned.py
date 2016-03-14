import sys, json, urllib2

link = 'https://haveibeenpwned.com/api/v2/breachedaccount/%s' % raw_input('Enter your email: ')

try:
    response = urllib2.urlopen(link)
    data = response.read()
    
except Exception:
    sys.exit('You were not pwned. You are safe :)')

parsed = json.loads(data)
print 'you were pwned at the following breaches:\n'

count = 1
for pwns in parsed:
    print '%2d) %-30s %s' %(count, pwns['Name'], pwns['Domain'])
    count += 1

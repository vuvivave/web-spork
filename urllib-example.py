'''

url = 'http://api.site.com/method/'
values = {'argument1': 'value1',
          'argument2': 'value2'}
data = urllib.parse.urlencode(values)
print(data)
'''

import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python'}

data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
import json
import urllib.request


#check out SSL
#===================SSL certificate errors=====================>
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#================================================>
url = 'https://healthdata.gov/data.json'
webURL = urllib.request.urlopen(url, context=ctx)
data = webURL.read()
encoding = webURL.info().get_content_charset('UTF-8')
json.loads(data.decode(encoding))

print(data)


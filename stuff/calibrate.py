import http.client

#==========SSL Certificate====================>
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#============================================>

conn = http.client.HTTPSConnection("sandbox-api.dexcom.com")

headers = {
    'authorization': "Bearer {your_access_token}",
    }

conn.request("GET", "/v2/users/self/calibrations?startDate=2017-06-16T08:00:00&endDate=2019-04-17T08:00:00", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
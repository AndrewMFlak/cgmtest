import http.client

#==========SSL Certificate====================>
# import ssl
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

#============================================>

print('<=============token.py file run check=============>')

conn = http.client.HTTPSConnection("sandbox-api.dexcom.com")

payload = "client_secret=VrzchNFWMq0Cl2mg&client_id=LzDLAxI7b2vDJSmRYuL8ry0VABo8AAel&refresh_token={your_refresh_token}&grant_type=refresh_token&redirect_uri=http://localhost/callback"
print(payload)
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

conn.request("POST", "/v2/oauth2/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
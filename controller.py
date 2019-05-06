# Get calibrations request
import http.client

# conn = http.client.HTTPSConnection("api.dexcom.com")

# sandbox enpoint https
#  https://sandbox-api.dexcom.com
conn = http.client.HTTPSConnection("sandbox-api.dexcom")

headers = {
    'authorization': "Bearer {your_access_token}",
    }

conn.request("GET", "/v2/users/self/calibrations?startDate=2018-04-30T08:00:00&endDate=2019-05-06T08:00:00", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
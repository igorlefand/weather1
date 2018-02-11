import requests
## /c/Users/mcse/AppData/Local/Programs/Python/Python36-32/Scripts/pip
## http://maps.googleapis.com/maps/api/geocode/json?address=haifa

place = input("Enter place name :")
#request altitude and longtitude from google
requestStringGoogle = ("http://maps.googleapis.com/maps/api/geocode/json?address=" + place)
resp =requests.get(requestStringGoogle)
if resp.status_code != 200:
    # This means something went wrong.
    raise requests.RequestException('GET ERROR {}'.format(resp.status_code))
g_resp = resp.json()
location = g_resp["results"][0]
altitude = location["geometry"]["location"]["lat"]
longtitude = location["geometry"]["location"]["lng"]
#print (altitude)
#print (longtitude)
#request 
requestStringDarksky = (f"https://api.darksky.net/forecast/0d584daf877a4ff2998afe4329840ef9/{altitude},{longtitude}" + "?units=si")
resp = requests.get(requestStringDarksky)
if resp.status_code != 200:
    # This means something went wrong.
    raise requests.RequestException('GET ERROR {}'.format(resp.status_code))

j_resp = resp.json()
print (f"Temp in {place} is:")
print(j_resp["currently"]["temperature"])
print (f"Humidity in {place} is:")
print (j_resp["currently"]["humidity"])
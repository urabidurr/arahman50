import urllib.request
import json

key = "qwpwSA84bvVv5XIbydb87537ZfpYRJkJlMEVddjH"
request = "https://api.nasa.gov/planetary/apod?api_key=qwpwSA84bvVv5XIbydb87537ZfpYRJkJlMEVddjH"


print("hello")

request_url = urllib.request.urlopen('https://www.geeksforgeeks.org/')
print(request_url.read())
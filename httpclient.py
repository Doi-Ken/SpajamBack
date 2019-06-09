import httplib, urllib
import json

def get(host, url):
    conn = httplib.HTTPConnection(host)
    conn.request("GET", url)
    response = conn.getresponse()
    print response.read()

def post(host, url, data):
    headers = {"Content-type": "application/json",  "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host)
    conn.request("POST",url, json.dumps(data), headers)
    response = conn.getresponse()
    print response.read()
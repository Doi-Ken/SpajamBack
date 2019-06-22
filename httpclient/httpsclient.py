import httplib
import json

def get(host, url):
    conn = httplib.HTTPSConnection(host)
    conn.request("GET", url)
    response = conn.getresponse()
    print response.read()

def post(host, url, data):
    headers = {"Content-type": "application/json",  "Accept": "text/plain"}
    conn = httplib.HTTPSConnection(host)
    conn.request("POST",url, json.dumps(data), headers)
    response = conn.getresponse()
    print response.read()

def post_jpeg(host, url, data):
    headers = {"Content-type": "image/jpeg"}
    conn = httplib.HTTPConnection(host)
    conn.request("POST", url, data, headers)
    response = conn.getresponse()
    print response.read()
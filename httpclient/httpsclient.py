import httplib
import json
import urllib2
import requests
import os

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

def post_jpeg(url):
    headers = {'Content-Type' : 'image/jpeg'}
    url = 'http://file.api.wechat.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE'
    files = {'media': open('test.jpg', 'rb')}
    response = requests.post(url, data=files, headers=headers, verify=False)
    print response

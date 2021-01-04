#!/usr/bin/python
import requests
import base64
import json
url = "https://www.hackthebox.eu/api/invite/generate"
i = 0 
num = int(input('Enter the number of invite codes: ')) 
while i < num :
        headers = {'User-Agent': ''}
        result = requests.post(url,headers=headers)  
        data = json.loads(result.text)
        parse = data['data']['code']  
        print(base64.b64decode(parse))
        i = i + 1


#references

# Here i didnt used any user agent , because it was working fine witout any 
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5'
# https://realpython.com/python-json/
# https://stackoverflow.com/questions/3470546/python-base64-data-decode



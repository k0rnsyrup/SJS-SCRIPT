import requests
import time
from random import *
import random
import json
import bs4
import datetime
from log import log as log
from bs4 import BeautifulSoup as soup
from fake_useragent import UserAgent
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from python3_anticaptcha import NoCaptchaTaskProxyless, NoCaptchaTask
from colorama import Fore, init


def enter_raffle(email):

    log('i', "Signing up with email <" + email + ">.")
    sess = requests.Session()
    ua = UserAgent()

    currentDT = datetime.datetime.now()

    timing = currentDT.strftime("%Y-%m-%d"+"T"+"%H:%M:%S"+"-04:00")



    link = "https://slamjamsocialism-drops.com/graphql"
    anti_api_key = "57d2dcc5417a508d191b7c92186e7bee"
    site_key = "6LfYhz0UAAAAAJFKp28Sg0NnAEIPMfKI1RJSGsdB"
    client = AnticaptchaClient(anti_api_key)
    task = NoCaptchaTaskProxylessTask(link, site_key)
    job = client.createTask(task)
    job.join()
    captcha = job.get_solution_response()


    headers = {

    "authority": "slamjamsocialism-drops.com",
    "method": "POST",
    "path": "/graphql",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "null",
    "content-type": "application/json",
    "dnt": "1",
    "origin": "https://slamjamsocialism-drops.com",
    "referer": "https://slamjamsocialism-drops.com/drops/140",
    "user-agent": str(ua.Chrome)

    }

    r = sess.get("https://slamjamsocialism-drops.com/drops/140", headers=headers)
    #print(r.headers)
    #print(r.request.headers)
    #print(r.cookies)

    data = {  
       "query":"mutation RequestOrdertMutation($data: OrderRequestInput!) {\n  requestOrder(data: $data)\n}\n",
       "operationName":"RequestOrdertMutation",
       "variables":{  
          "data":{  
             "firstName":first_name,
             "lastName":last_name,
             "email":email,
             "phone":phone,
             "country":"840",
             "city":city,
             "order":[  
                {  
                   "product":"115",
                   "size":size
                }
             ],
             "raffle":"140",
             "captcha": captcha,
             "date":str(timing)
          }
       }
    }

    proxy_list =[
        "US-10m.geosurf.io:10001",
        "US-10m.geosurf.io:10002",
        "US-10m.geosurf.io:10003",
        "US-10m.geosurf.io:10004",
        "US-10m.geosurf.io:10005",
        "US-10m.geosurf.io:10006",
        "US-10m.geosurf.io:10007",
        "US-10m.geosurf.io:10008",
                              #enter like this separate with commas
        ]    

    random_proxy = random.choice(proxy_list)
        
    proxy= {
           "http": random_proxy
           }            




    response = sess.post("https://slamjamsocialism-drops.com/graphql", headers=headers, json=data, proxies=proxy)
    print(response.status_code)
    print(response.content)
    content_type_header = response.headers.get('content-type')
    #parsed = json.loads(response.content.decode('utf8'))
    #parsed = response.text.decode('utf8')
    #print(parsed
    flag = b'\x83\x0e\x00\x00\x04\x9aq\xe4/\x98H"\x1bH\xda\xd5\x92LR\xca,\xea:-\x95%T\xc0\x9d\xfb\xa0t\xc16' in response.content
    
    return flag


if(__name__ == "__main__"):
    # Ignore insecure messages
    requests.packages.urllib3.disable_warnings()

    # User settings
    first_name = "jordan"
    last_name = "korn"
    city = "new cumberland"
    size = "45" #look at the site for the sizes
    domain = "@kornkicks.club"

    entries = 100 #change this depending on how many proxies you have

    for count in range(0, entries):
        email = "zalman" + str(count) + domain
        phone = randint(1111111111, 9999999999)
        success = enter_raffle(email)
        
        if(success):
            log('s', "Entry under email <" + email + "> succeeded.")
        else:
            log('e', "Entry under email <" + email + "> failed.")
        
        time.sleep(3)


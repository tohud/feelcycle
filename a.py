from bs4 import BeautifulSoup as bs4
import requests
import json

MYPAGE="https://www.feelcycle.com/feelcycle_reserve/mypage.php"

def feelCycleReserver():
    s=requests.Session()
    r=s.get(MYPAGE)
    r.encoding=r.apparent_encoding
    res_cookies=(r.headers)['Set-Cookie']
    phpCookie=s.cookies.get("PHPSESSID")
    phpCookies=dict(PHPSESSID=phpCookie)
    #tmp=bs4(r.text,features="html.parser")
    return(r.text)

    if "a"=="b":
        payload={
            'login_id':'id',
            'login_pass':'pass',
            'commit_login':''
        }
        r=s.post(MYPAGE,data=payload,cookies=phpCookies)
        r.encoding=r.apparent_encoding
        print(r.text)

        soup=bs4(r.text,features="html.parser",from_encoding="utf-8")
        print(soup)

def lambda_handler(event, context):
    # TODO implement
    res=feelCycleReserver()
    return {
        'statusCode': 200,
        #'body': json.dumps('Hello from Lambda!')
        'body': json.dumps(res)
    }

if __name__ == '__main__':
    feelCycleReserver()

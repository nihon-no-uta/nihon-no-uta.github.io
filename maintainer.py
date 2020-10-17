import requests
from pyngrok import ngrok
from requests.packages.urllib3.exceptions import ProtocolError

code = '8c73f59903fa.ngrok.io'
flag = False
try:
    response = requests.get(code)
    if response.status_code == 404:
        flag = True
        print('SITE DOWN: due to ngrok')
    elif response.status_code == 200:
        print('SITE UP')
    elif response.status_code == 502:
        print('SITE DOWN: code not running')
    else:
        print(response.status_code)
except (ConnectionError, ProtocolError, SocketError):
    print("Unknown E")

if flag == True:
    public_url = ngrok.connect()

public_url = 'http://a16de191bfaf.ngrok.io"'
index = open('index.html').read()
new_index = ''
for line in index.split('\n'):
    if 'meta http-equiv = "refresh" content = "2; url' in line:
        # print(line)
        temp = line.split()
        for i,_ in enumerate(temp[1:-1]):
            if temp[i-1] == 'url' and temp[i] == '=':
                temp[i+1] = public_url
        temp = ' '.join([itm for itm in temp])
        # print(temp)
        new_index += (temp +'\n')
    else:
        new_index += (line +'\n')

f = open('new_index.html',"w")
f.write(new_index)
f.close()
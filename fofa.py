import json
import sys
import requests
from pathlib import WindowsPath
from requests.packages import urllib3
result2=[]
def fofasearch(email,key,base64key,value):
    url="https://fofa.so/api/v1/search/all?email="+email+"&key="+key+"&qbase64="+base64key+"&size="+value
    res=json.loads(requests.get(url).text)
    result=res["results"]
    for i in range(len(result)):
        result2.append(result[i][0])


def fofahttp():
    fofahttpslist=[]
    fofahttplist=[]
    for line in result2:
        if 'https' in line:
            fofahttpslist.append(line)
        elif ':443' in line:
            newline='https://'+line
            fofahttpslist.append(newline)
        else:
            fofahttplist.append(line)          
    with open('./fofahttps.txt','w') as f:
        for line in fofahttpslist:
            f.write(str(line)+'\n')
        for line in fofahttplist:
            f.write('http://'+str(line)+'\n')

def fofalist():
    fofalist=[]
    for line in result2:
        if 'https' in line:
            newline=line.split("https://")[1]
            if ':' in newline:
                fofalist.append(newline)
            else:
                line=newline+':443'
                fofalist.append(line)
        else:
            fofalist.append(line)     
    with open('./fofa.txt','w') as f:
        for line in fofalist:
            f.write(str(line)+'\n')



if __name__=="__main__":
    email=sys.argv[1]
    key=sys.argv[2]
    base64key=sys.argv[3]
    value=sys.argv[4]
    fofasearch(email,key,base64key,value)
    fofahttp()
    fofalist()


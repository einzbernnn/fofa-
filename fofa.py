from pathlib import WindowsPath
import requests
from requests.packages import urllib3
import json
import sys
result2=[]

def fofasearch(email,key,base64key,value):
    url="https://fofa.so/api/v1/search/all?email="+email+"&key="+key+"&qbase64="+base64key+"&size="+value
    res=json.loads(requests.get(url).text)
    result=res["results"]
    for i in range(len(result)):
        result2.append(result[i][0])
    with open('./fofa.txt','w') as f:
        for line in result2:
            f.write(str(line)+'\n')

if __name__=="__main__":
    email=sys.argv[1]
    key=sys.argv[2]
    base64key=sys.argv[3]
    value=sys.argv[4]
    fofasearch(email,key,base64key,value)

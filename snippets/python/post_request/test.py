# -*- coding: utf-8  

import sys
import json
import urllib2

data = "해당 문장은 트위터 형태소 분석기의 테스트를 위한 문장입니다."
data = "그놈의 물욕센서(...)"
data = "외쳐 괴~!! 조~!!"

url = 'http://ec2-54-183-216-199.us-west-1.compute.amazonaws.com:8081'
req = urllib2.Request(url + '/api/v1/tokenizeSpeechParts/true/true')

reload(sys)
sys.setdefaultencoding("utf-8")

req.add_header('Content-Type', 'text/plain')
response = urllib2.urlopen(req, json.dumps(data,ensure_ascii=False).encode('utf8'))
data = response.read()
morphemes = json.loads(data)

for i in range(1,len(morphemes)-1):
    morpheme = morphemes[i]
    print morpheme["token"], morpheme["type"]

import json
import re

f = open("vuln.txt", "r")
countLow = 0  
countMed = 0
countHigh = 0
countTotal = 0
lowVuln = []
medVuln = []
highVuln = []
cmsInfo = []

c = f.readlines()

for i in c:
    line = i[3::].strip()
    
    if i[1] == "L":
        lowVuln.append(line)
        countLow += 1
       
    elif i[1] == "M":
        medVuln.append(line)
        countMed += 1

    elif i[1] == "H":
        highVuln.append(line)
        countHigh += 1
    
    elif i[1] == "I":
        cmsInfo.append(line)

countTotal= countLow + countMed + countHigh

#data = {'data': [{'Low-vulnerability': lowVuln, 'Medium-vulnerability': medVuln, 'High-vulnerability': highVuln, 'Cms-info': cmsInfo, 'countLow': countLow, 'countMed': countMed, 'countHigh': countHigh, 'countTotal': countTotal}]}
#data = {'data': [{'Low-vulnerability': lowVuln, 'Medium-vulnerability': medVuln, 'High-vulnerability': highVuln, 'Cms-info': cmsInfo}] , 'chart':[['countLow', countLow], ['countMed', countMed] , ['countHigh', countHigh], ['countTotal', countTotal]]}
data =  [['countLow', countLow], ['countMed', countMed], ['countHigh', countHigh], ['countTotal', countTotal], 'data': [{'Low-vulnerability': lowVuln, 'Medium-vulnerability': medVuln, 'High-vulnerability': highVuln, 'Cms-info': cmsInfo}] ]
jsondata = json.dumps(data, indent=4)

fName = c[0]
a = fName.split()

filename = a[1]
url = re.compile(r"https?://(www\.)?")

filenames = url.sub('', filename).strip().strip('/')
filenames = filenames.replace(".", "_") + ".json"

f = open(filenames,"w+")
f.write(jsondata)
f.close()
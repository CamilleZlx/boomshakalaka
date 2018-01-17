#python3.6

f = open('C:/Users/Camille/Desktop/Python3/read.txt','r',encoding='utf-8')
lines = f.readlines()
urlData = []
#print(urlData)
for line in lines:
    print(line)
    temp = line.replace('\n','')
    print(temp)
    urlData.append(temp.replace('\ufeff',''))
start_URL = urlData
print(start_URL)
print(urlData)
#python2.7
import  urllib2

#response = urllib2.urlopen("http://www.baidu.com")
#print response.read()

request = urllib2.Request("http://www.baidu.com")
response = request.urlopen(request)
print response.read()
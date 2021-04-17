import urllib.request
import urllib.parse


#url = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php')

#print(url.read())

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
num = "12345"
content = urlopen(uri %num).read().decode()
print(content)
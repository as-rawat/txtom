import sys
import urllib2

type = "+lyrics"
q = sys.argv[1].replace(" ", "+")
site = "https://www.google.com/search?q=%s%s"%(q,type)

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'} 

request = urllib2.Request(site, headers=header)

try:
  page = urllib2.urlopen(request)
except urllib2.HTTPError, e:
  print e.fp.read()

content = page.read()

index = content.find("kno-ecr-pt kno-fb-ctx")

if index != -1:
  tval = content[index:]
  index1 = tval.find(">") + 1
  index2 = tval.find("<")
  val = tval[index1:index2]
  print val,
  print " - ",
  index = tval.find("a href")
  tval = tval[index:]
  index1 = tval.find(">") + 1
  index2 = tval.find("<")
  val = tval[index1:index2]
  print val
elif content.find(" - YouTube") != -1:
  index = content.find("- YouTube")
  tval = content[:index]
  index1 = tval.rfind(">") + 1
  index2 = index - 1
  val = tval[index1:index2]
  print val
else:
  print "Not found."



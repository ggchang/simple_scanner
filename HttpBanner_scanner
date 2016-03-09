#！/usr/bin/python
#by--ggchang

import urllib
import os,sys

def check(url):
    try:
        req=urllib.urlopen("http://"+url)
        info = req.info()
        webServerType = (info.dict)['server']
        print url + " : " + webServerType
    except Exception, e:
        print str(e)

if __name__ == '__main__':
    ipList = sys.argv[1]
    openfile = open(ipList,'r')
    for read in openfile.readlines():
        read = read.strip()
        check(read)

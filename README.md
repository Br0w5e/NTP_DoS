# NTP_DoS
a script for NTP_DoS
## 仅供学习参考，学习后请立即删除。切勿用于非法用途！！！！  


## 步骤
### 1）扫描
扫描发现命令masscan
```bash
sudo apt-get install masscan
masscan -pU:123 -oX ntp.xml --rate 160000 101.0.0.0-111.111.111.111
```
后边的网段是自己添加的，完全可以使用服务器进行全网扫描的（太慢了！）
### 2）去重
有时候会发现扫描后得到的服务器有重复的，这时候我们需要进行去重处理！使用quchong.py
### 3）IP筛选
找出运行ntp服务的IP，根据是否响应MONLIST命令得出结论！使用shaxuan.py
### 4）测试
使用在生成的monlistServers.txt选择服务器进行ntp抗压测试！

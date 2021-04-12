# portscan

用于探测IP与端口开放情况，默认扫描1-10000端口

支持C段、B段、A段探测，速度较快。流量较小。

探测结果讲开放的IP与端口保存在同目录下的“ip-port.txt”中。
保存内容格式为：192.168.0.1:80


v2 版本可以扫描指定端口
命令：python portscan-v2.py 172.16.24.1/24 3389

![Image text](hhttps://github.com/d3ckx1/portscan/blob/main/截屏2021-04-12%20上午10.01.43.png)

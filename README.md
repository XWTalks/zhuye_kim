# zhuye_kim
仿zhuye.kim的简单导航程序

演示地址：http://118.25.14.156:8080

[![20180716212904.png](https://i.loli.net/2018/07/16/5b4c9efbf04ca.png)](https://i.loli.net/2018/07/16/5b4c9efbf04ca.png)

#### 使用说明 ####


- 安装Python3和必备组件、库

Centos7系统安装Python3可以参考文章：http://blog.51cto.com/wenguonideshou/2083301

```bash
yum install git screen -y
pip3 install django pymysql pillow
```

- 安装mysql/mariadb，新建数据库名为zhuye

- 修改zhuye_kim/settings.py中的DATABASES对应的数据库信息（只需要修改数据库密码）

- 下载源码、建表

```bash
git clone https://github.com/wenguonideshou/zhuye_kim
cd zhuye_kim
python3 manage.py makemigrations
python3 manage.py migrate
```

- 导入zhuye.sql

- 运行网站
```bash
screen -S zhuye
python3 manage.py runserver 127.0.0.1:8001
```
Nginx反向代理

![20180717220239.png](https://i.loli.net/2018/07/17/5b4df8524ab67.png)


后台地址为http://ip/admin，如果已经反向代理则是http://域名/admin，管理员用户名admin密码12345678@

后台的“大分类”指的是常用/男生/女生 这一行，“小分类”指的是热门/资讯/影音/邮箱的这一列

**获取更多帮助请[加群](http://shang.qq.com/wpa/qunwpa?idkey=d119da6023cc49729a61139ca4b8bb0ee770d8d9a89383939c4a45159f82bc6d)**

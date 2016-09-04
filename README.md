# SinaL2
从dHydra框架( https://github.com/Emptyset110/dHydra )
中抽离出来的获取Sina Level2行情/逐笔的类

## 注意事项
 - 在新浪购买Level2数据时有声明，禁止恶意抓取，不保证在云服务器的可用性，数据可靠性与使用方式的最终解释权属于新浪。 dHydra不拥有任何解释权。
 - 由于这是直接从dHydra中去耦合抽离出来的逻辑，为了省事我并没有去掉安装时候的依赖包。（比如依赖了pandas这种大的安装包，个人认为装一下也没什么不好，虽然基本用不到）
 - 最后，还是建议采用dHydra框架，对于高频数据的处理做好了redis等方案
 - **采用Apache开源协议**


## 使用方法
用pip安装
```
pip install SinaL2
```

或者
```
git clone https://github.com/Emptyset110/SinaL2.git
cd SinaL2
```

## 在运行当前目录新建文件`sina.json`来配置你的新浪帐号信息（需要在新浪购买Level2,普及版或标准版通用）
```
{
	"username":"",
	"password":""
}
```

## 使用范例
```python
from SinaL2 import SinaL2

# 这是websocket收到数据以后的回调函数，将它传入SinaL2即可
def on_recv_data(message):
    print(message)

# symbols为传入的代码list，list长度任意
sina_l2 = SinaL2(symbols=["sz000001"], on_recv_data = on_recv_data)
sina_l2.start()
```

> 详细参数说明还是参考( https://github.com/Emptyset110/dHydra )或者( http://doc.dhydra.org )

# DataSpider

DataSpider是一个供第三方开发者使用的万能爬虫库。第三方开发者可以实例化其中Spider类，然后使用该类来进行数据抓取、存储等操作。

由于学校急催找工作的原因，以及精力和时间多因素的影响，该项目目前就写到这里，已经具备基本的爬虫能力，支持自定义规则、存储功能等等。

## 1. 复制

最简单的使用方式就是将`data_spider包`以及`requirements.txt`复制到项目的根目录下，在根目录下打开终端，运行以下pip命令：

```bash
pip install -r requirements.txt -i [推荐使用国内镜像源]
```

最后删除`requirements.txt`文件。

## 2. 导入

```python
from data_spider import *
```
## 3. 详见DS使用文档

1、django 在单独文件 中加载django环境临时调试

创建Django环境后,每次在打印调试都需要基于项目有些麻烦.

如何在项目外的文件中加载项目环境进行便携的调试?

　　创建一个新的 orm.py

```python
import os

if __name__ == '__main__':
# 加载Django项目的配置信息　　
# 看起来有点长, 不过此命令可以在项目的 manage.py 的第 7 行直接拿来用
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ormday69.settings")
# 导入Django，并启动Django项目
import django
django.setup()

# 然后就可以直接通过此py文件进行调试了
from app01 import models
ret = models.Person.object.all()
print(ret)
```




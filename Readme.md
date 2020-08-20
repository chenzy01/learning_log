## 学习笔记
### Django 项目

环境：Windows10 Python3

项目：learning_log  

#### 创建虚拟环境及项目

1. 创建工作目录
- mkdir learning_log

虚拟环境：ll_env

2. 创建虚拟环境
- python -m venv ll_env/  （Wnidows 系统）
- virtualenv ll_env/ (Linux 中用法)  

3. 激活虚拟环境
- source ll_env/Scripts/activate （Wnidows 系统）
- source ll_env/bin/activate (Linux 中用法)  

停止使用虚拟环境
- deactivate  

升级安装工具
- python -m pip install --upgrade pip (在虚拟环境中)
- python.exe -m pip install --upgrade pip (先切换到python的安装目录下)

4. 创建项目(在虚拟环境激活的前提下)
$ django-admin.py startproject learning_log .   (切忌不要忘记最后还有一个点，该点的作用，可在开发完成后方便将应用
部署到服务器)  
创建完项目后，根目录 learning_log 下面包含的文件：  
- learnging_log 项目
- ll_env  虚拟环境
- manage.py 接受命令并将其交给 Django 的相关部分去执行
  
learnging_log 文件夹下面包含的文件：    
- __init__.py  空文件夹，表示 learnging_log 目录是 python 的标准包
- setting.py 指定 Django 如何与系统进行交互和如何管理项目，配置文件，包含Django 模块应用配置、数据库配置、模板配置等
- urls.py 告诉 Django 应创建哪些网页来响应浏览器请求，定义 URLconf
- wsgi.py(wsgi: web server gateway interface Web 服务器网关接口) 帮助 Django 提供它创建的文件，提供服务的入口

#### 创建数据库及应用

1. 创建数据库(迁移数据库)
- $ pyton manage.py migrate  

Django 默认使用 sqllite 数据库,以上命令执行完成后，根目录 learning_log 下面包含的文件：  
- learnging_log 项目
- ll_env  虚拟环境
- manage.py 接受命令并将其交给 Django 的相关部分去执行
- db.sqlite3 存储项目的数据

2. 创建应用程序
- 命令：python manage.py startap appname （在 manage.py 所在的目录下面执行该命令）
$ python manage.py startapp learning_logs  
应用上面的命令后，创建了应用程序所需的基础设施  
- __init__.py
- admin.py  映射 models 中的数据到 Django 自带的后台 
- apps.py  用于应用程序配置  
- migrations 这是目录，存放初始化模型的内容以及对models.py的改动
- models.py  定义要在应用程序中管理的数据，告诉 Django 如何执行。代码层面，一个模型就是一个类，经过迁移后，对应数据库中的一张表
- tests.py  用于进行单元测试
- views.py  视图文件，控制向前端输送内容


3. 在 learning_log/setting.py 中，找到 INSTALLED_APPS ，这里告诉 Django 哪些应用程序安装在项目中，  
前面新建的应用 learning_logs 也必须添加到这里  

```python
# 告诉 Django 哪些应用程序安装在项目中
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 添加了 learning_logs 应用程序
    'learning_logs',
]
```

4. 对应用修改数据库，创建模型，创建表，使其能够存储与模型 Topic 相关的信息
```python
$ python manage.py makemigrations learning_logs  
# 作用：让 Django 确定如何修改数据库，使其能够存储与定义的新模型相关联的数据 
# makemigrations 操作记录下所有关于modes.py的改动，但该改动没有作用到数据库
```
执行完上面的命令后，会在 learning_logs/migrations 下面初始化模型，多了两个文件  
- 0001_initial.py 迁移文件，后面的 migrate 命令会根据这个文件，在数据库中给模型 Topic 创建一个表
- __init__.py  

执行迁移命令,注意最下面一行提示  
```python
$ python manage.py migrate  
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0001_initial... OK
```
migrate 作用，将当前的migration文件内容持久化到数据库中，比如创建表，修改字段的类型等  
官方文档解释：makemigrations 命令负责保存你的模型变化到一个迁移文件，同时 migrate 负责将改变提交到数据库。
若数据库发生改变需要修改数据，采取的三个步骤：
- 修改 models.py
- 对应用调用 makemigrations
- 对 Django 迁移项目，使用 migrate 命令

#### 管理网站

1. 创建超级用户  
- $ python manage.py createsuperuser  

Django 自动在管理网站添加了 User 和 Group 模型  
对于 Topic 模型，仍需要手工创建  
```python
from django.contrib import admin
from learning_logs.models import Topic

# Register your models here.
admin.site.register(Topic)
```

定义 Entry 模型  

```python
class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta 存储用于管理模型的额外信息"""
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."
```

迁移 Entry 模型  

```python
# 因添加了一个新模型，需要再次修改(迁移)数据库
$ python manage.py makemigrations learning_logs
Migrations for 'learning_logs':
  learning_logs\migrations\0002_entry.py  # 新的迁移文件 0002_entry.py，告诉 Django 如何修改数据库
    - Create model Entry
```

启动一个Python解释器，并查询项目数据库中的数据  

```python
$ python manage.py shell
>>> from learning_logs.models import Topic
>>>Topic.objects.all()
```



#### 创建学习笔记主页

1. 定义 url 

定义主页的地址  
url 函数参数解析： 
1. r'^$' 正则表达式，Django 在 urlpatterns 中查找与请求的URL字符串相匹配的正则表达式，
，所以正则表达式定义了 Django 可查找的模式， 
r 表示把字符串当做原始字符串，
'' 引号表示正则表达式从哪开始,从哪结束
^ 脱字符，让python查看字符串的开头
$ 美元符号让python查看字符串的结尾
该正则表达式与基础url相匹配：http://localhost:8000/
2. views.index 指定了要调用的视图函数  
3. name='index' 将这个url模式的名称指定为 index，以便代码在其他地方可以引用

```python
from django.conf.urls import url  # 用 url 函数 将地址映射到视图

from . import views  # 从当前 urls.py 所在的目录下，导入 views（视图）

# 该模块定义了可在管理网站中请求的所有URL
# learning_logs.urls 模块的urls，还定义了 namespace ，将 learning_logs 的url与项目中的其它url区分开来
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('learning_logs.urls', namespace='learning_logs')),
]
```

2. 编写视图

Django 在文件 views.py 中查找函数 index()，再将请求对象传递给这个视图函数  
render() 提供两个实参：  
1. 原始请求对象
2. 可用于创建网页的模板

```python
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')
```

3. 编写模板 
模板定义了网页的结构，模板一般存在在项目的 templates 目录下，因此在 templates 下创建 learning_logs，
在 learning_logs 下面创建 index.html 。 这样做的好处是将 URL、视图和模板分离开来，当项目扩大时，可以考虑
不同方向，且让参与者可以专注其擅长的方向，分工明确。
index.html 
```html
<p>Learning Log</p>

<p>Learning Log helps you keep track of yhour learning, for any topic you`re learning about</p>
```

#### 创建其他网页

该部分扩充了两个显示数据的新网页。首先创建了一个父模板HTML，新的网页都继承这个父模板来显示数据，其中一个
显示所有特定主题，另一个显示所有主题的条目 

1. 




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
- pyton manage.py migrate  Django 默认使用 sqllite 数据库


2. 创建应用程序
- 命令：python manage.py startap appname （在 manage.py 所在的目录下面执行该命令）
$ python manage.py startapp learning_logs  
应用上面的命令后，创建了应用程序所需的基础设施  
- __init__.py
- admin.py
- apps.py
- migrations 
- models.py  定义要在应用程序中管理的数据，告诉 Django 如何执行。代码层面，一个模型就是一个类
- tests.py
- views.py


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


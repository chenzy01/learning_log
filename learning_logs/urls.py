"""定义 learning_logs 的 URL 模式"""

from django.conf.urls import url  # 用 url 函数 将地址映射到视图

from . import views  # 从当前 urls.py 所在的目录下，导入 views（视图）

"""
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
"""
urlpatterns = [
    url(r'^$', views.index, name='index'),  # 让python查找开头和末尾之间没有任何东西的url
    url(r'^topics/$', views.topics, name='topics'),
]

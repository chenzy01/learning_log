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
    # 让python查找开头和末尾之间没有任何东西的url
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    # topic_id与某个主题对应，以此来捕获一个数字值，存储在topic_id中
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]

"""
r'^topics/(?p<topic_id>\d+)/$' 解析：
r 表示原始字符串，并指出正则表示式包含在引号内
/(?p<topic_id>\d+)/  结合前面的 topics 一起匹配，这里的部分是匹配一个整数值，并将值存储在 topic_id的实参中
() 捕获URL中的值
?p<topic_id>\d+  将匹配到的值存储到 topic_id 中
\d+ 匹配任何数字，不管这个数字有多少位
"""

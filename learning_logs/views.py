from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm


# Create your views here.


def index(request):
    """学习笔记主业
    Django 在文件 views.py 中查找函数 index()，再将请求对象传递给这个视图函数
    render() 提供两个实参：
    1. 原始请求对象
    2. 可用于创建网页的模板
    """
    return render(request, 'learning_logs/index.html')


def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """显示单个主题极其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')  # - date_added 前面的减号指定按降序排序
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """添加新主题
    根据请求类型，判断用户是的请求是空表单(get 请求),还是要求对填写好的表单进行处理(post 请求)
    """
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST 提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():  # 检查用户填写的表单是否有效，输入的数据是否与要求的一致
            form.save()  # 将有效的表单信息写入数据库
            return HttpResponseRedirect(reverse('learning_logs:topics'))
            # 用户提交主题后，使用HttpResponseRedirect这个类将用户重定向到网页topics。
            # reverse() 函数根据指定的url模型确定url

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

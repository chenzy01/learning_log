from django.shortcuts import render
from .models import Topic


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

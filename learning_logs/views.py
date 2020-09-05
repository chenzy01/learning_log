from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.


def index(request):
    """学习笔记主业
    Django 在文件 views.py 中查找函数 index()，再将请求对象传递给这个视图函数
    render() 提供两个实参：
    1. 原始请求对象
    2. 可用于创建网页的模板
    """
    return render(request, 'learning_logs/index.html')


# 检查用户查看主题前是否已经登录，没有就跳转到登录页面
@login_required()
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required()
def topic(request, topic_id):
    """显示单个主题极其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')  # - date_added 前面的减号指定按降序排序
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required()
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


@login_required()
def new_entry(request, topic_id):
    """在特定的主题添加新条目"""
    topic = Topic.objects.get(id=topic_id)  # 获取主题

    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EntryForm()
    else:
        # POST 方式提交数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():  # 检查表单是否有效
            new_entry = form.save(commit=False)  # commit=False,因此不会保存到数据库中，保存在属性new_entry中
            new_entry.topic = topic  # 由Topic获取到
            new_entry.save()  # 保存后，条目就与特定的主题关联
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required()
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)  # 获取用户要修改的条目对象
    topic = entry.topic

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
        # 使用实参 instance 创建一个EntryForm实例，该实参让Django创建一个表单，data 不写，使用默认值，即现有的条目填充data
    else:
        # POST 提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

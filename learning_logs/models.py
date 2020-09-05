from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Model 定义了模型基本功能的类
class Topic(models.Model):
    """用户学习的主题"""
    # CharField 由字符或文本组成的数据，它必须告诉Django在数据库中预留多少空间
    text = models.CharField(max_length=200)
    # DateTimeField 记录日期和时间的数据，auto_now_add=True 该属性在用户创建主题时，就会自动设置成当前日期和时间
    date_added = models.DateTimeField(auto_now_add=True)
    ower = models.ForeignKey(User)  # 建议与模型User的外键关系

    def __str__(self):
        """返回模型的字符串表示"""
        # __str__() 方法的作用：让 Djanog 在加载某个表时，想显示什么属性，它返回的东西必须
        # 是一个字符串对象，
        # 若打印 Topic 类的实例对象时，会自动调用__str__() 方法
        return self.text


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

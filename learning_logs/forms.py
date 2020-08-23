from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        """指出表单基于的模型，以及要在表单中包含哪些字段"""
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        """widget是一个HTML表单元素，通过设置widgets，可覆盖Django选择的默认小组件。
        attrs={'cols': 80} 将文本区域的宽度设置为80列，默认是40列
        """
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

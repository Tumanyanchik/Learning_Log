from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Class determine topic forms"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """Class determine enry forms"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 90})}

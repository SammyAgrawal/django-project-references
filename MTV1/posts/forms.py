from django import forms

class TopicForm(forms.Form):
    topic = forms.CharField()

class ReplyForm(forms.Form):
    reply = forms.CharField(widget=forms.Textarea)
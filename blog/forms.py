from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'message',
                  'post']  # we want to show this field in form, we don't want to show approved

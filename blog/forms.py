from django import forms
from blog.models import Comment


from website.models import Contact, Newsletter


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['post','name', 'email', 'subject', 'message']


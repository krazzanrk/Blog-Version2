from django import forms


class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea())
    blog_comment_id = forms.IntegerField()

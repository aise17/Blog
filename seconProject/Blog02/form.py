from django import forms
from Blog02.models import Post, Comment
from django.shortcuts import redirect


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('category', 'title', 'body', 'status')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('title', 'body')

	
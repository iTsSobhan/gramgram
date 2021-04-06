from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('profile', 'title', 'photo')
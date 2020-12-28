from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField


class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	text = FroalaField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png', blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	
	def __str__(self):
		return self.title

	def textshot(self):
		return self.text[:50] + '...'
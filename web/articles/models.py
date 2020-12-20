from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	text = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png', blank=True)
	# add author
	
	def __str__(self):
		return self.title

	def textshot(self):
		return self.text[:50] + '...'
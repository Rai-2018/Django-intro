from django.db import models
from django.urls import reverse
# Create your models here.
class Article(models.Model):
	text = models.CharField(max_length=20)
	description = models.TextField(blank = True, null = True)

	def get_absolute_url(self):
		return reverse("article:article_detail1",kwargs={"id":self.id})
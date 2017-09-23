from django.db import models
from django.utils import timezone


#models.Model 表示 post是一个Django模型
# models.foreignkey 指向另一个模型的连接
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now
		self.save()

	def __str__(self):
		return self.title

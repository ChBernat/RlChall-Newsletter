from django.db import models

class Mails(models.Model):
	mail = models.EmailField()
	def __str__(self):
		return self.mail
class Message(models.Model):
	subject = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now=True)
	news_msg = models.TextField()
	def __str__(self):
		return self.title
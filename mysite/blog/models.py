from django.db import models

# Create your models here. - models.Model makes a table
class Post(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()
	
	def __str__(self):
		# Do this as otherwise it will retunr the computer memory location rather then the string.
		return self.title
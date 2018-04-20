from django.db import models

class Organisation(models.Model):
	name = models.CharField(max_length=200)
	inn = models.IntegerField()
	kpp = models.IntegerField(null=True, blank=True)
	
	def __str__(self):
		return self.name

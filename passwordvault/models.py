from django.db import models

# Create your models here.
class PasswordVault(models.Model):
	INTEGER_CHOICES= [tuple([x,x]) for x in range(6,16)]
	integer_value = models.IntegerField(default = 10) 
	include_numbers = models.BooleanField()
	include_lower = models.BooleanField()
	include_upper = models.BooleanField()
	include_symbols = models.BooleanField()

	exclude_similar = models.BooleanField()
	exclude_char = models.BooleanField()

	password = models.CharField(max_length=200)
	can_store = models.BooleanField()
	general_info = models.CharField(max_length=200)
	
	website = models.URLField(default='')
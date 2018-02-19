from django.db import models

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length='225')
	release_date = models.DateField()
	multiplayer = models.BooleanField()
	image = models.ImageField()

	PC = 'PC'
	phones = 'ph'
	Xbox = 'Xb'
	Web = 'Wb'
	platform_choices = (
		(PC, 'PC'),
		(phones, 'smartphones'),
		(Xbox, 'Xbox one'),
		(Web, 'Web Browser'),
	)
	platforms = models.CharField(max_length=2,choices=platform_choices,default='PC')

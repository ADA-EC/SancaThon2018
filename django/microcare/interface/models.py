from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class Device(models.Model):
    mac_address = models.CharField(primary_key=True, max_length = 17)
    last_position = models.CharField(max_length = 128)
    last_seen = models.DateTimeField(default=timezone.now)
    power = models.IntegerField(default=100)
    num_moves = models.IntegerField(default=0)

class Equipament(models.Model):
    name = models.CharField(max_length = 128)
    category = models.CharField(max_length=128)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

class Movement(models.Model):
	device = models.ForeignKey(Device, on_delete=models.PROTECT)
	old_position = models.CharField(max_length = 128)
	new_position = models.CharField(max_length = 128)
	when = models.DateTimeField(default=timezone.now)

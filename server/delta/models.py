from django.db import models
class status(models.Model):
    title=models.CharField(max_length=300)
    moisture=models.CharField(max_length=300)
    def __str__(self):
        return '%s %s' % (self.title, self.moisture)
class led(models.Model) :
    order=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    def __str__(self):
        return '%s %s' % (self.order, self.position)
# Create your models here.

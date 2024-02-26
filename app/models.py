from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField()
    satellite = models.CharField(max_length=255)
    color = models.CharField(max_length=255,default=1)
    count = models.IntegerField(default = 1)

    

    def __str__(self):
        return self.name
    



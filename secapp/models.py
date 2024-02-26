from django.db import models

class Street(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField(default=1)
    def __str__(self):
        return self.name
    


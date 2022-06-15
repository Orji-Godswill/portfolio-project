from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    role = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

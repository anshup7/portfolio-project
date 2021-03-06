from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')

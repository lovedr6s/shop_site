from django.db import models

# Create your models here.
class Shoes(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="shoes/")
    price = models.IntegerField()

    def __str__(self):
        return self.title

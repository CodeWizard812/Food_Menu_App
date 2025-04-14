from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_description = models.TextField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://cleanplatesdetroit.com/data/meals/1289.jpg")

    def __str__(self):
        return self.item_name
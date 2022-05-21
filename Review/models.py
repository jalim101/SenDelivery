from django.db import models
from cust.models import Client


# Create your models here.

class MyModel(models.Model):
    id = models.AutoField(primary_key=True)


class ReviewOrder(models.Model):
    Bad = 'Плохо'
    Good = 'Хорошо'
    Average = 'Пойдет'
    Worst = 'Ужасно'
    Excellent = 'Отлично'
    choices = (('Плохо', Bad), ('Хорошо', Good), ('Пойдет', Average), ('Ужасно', Worst), ('Отлично', Excellent))
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    review = models.TextField(default='', blank=True, max_length=1000)
    rating = models.CharField(choices=choices, default=Good, max_length=15)

    def __str__(self):
        return "{} - {}".format(self.client.user.username, self.rating)

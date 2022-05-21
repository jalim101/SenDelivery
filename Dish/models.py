from django.db import models
from django.contrib.auth.models import User

class MyModel(models.Model):
    id = models.AutoField(primary_key=True)


class MainDish(models.Model):
    EUROPEAN = 'European'
    BARMENU = 'Bar menu'
    BREAKFASTS = 'Breakfasts'
    SALADS = 'Salads'
    FIRSTCOURSE = 'First course'
    LAGMAN = 'Lagman'
    PIZZA = 'Pizza'
    EASTERN = 'Eastern'
    SNACK = 'Snack'
    MEAT = 'Steak Grill Shashlick'
    PANASIAN = 'Pan Asian'
    BAKERY = 'Bakery'
    GARNISH = 'Garnish Sauces'

    TYPE_CHOICES = [(EUROPEAN, 'European'), (BARMENU, 'Bar menu'), (BREAKFASTS, 'Breakfasts'), (SALADS, 'Salads'),(FIRSTCOURSE, 'First course'), (LAGMAN, 'Lagman'), (PIZZA, 'Pizza'), (EASTERN, 'Eastern'), (SNACK, 'Snack'), (MEAT, 'Steak Grill Shashlick'), (PANASIAN, 'Pan Asian'), (BAKERY, 'Bakery'), (GARNISH, 'Garnish Sauces')]


    name = models.CharField(max_length=40)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default=BARMENU)
    desc = models.TextField(max_length=1000)
    image = models.FileField(upload_to='dishes/images/')
    price = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.name, self.type)

# class Cust_Cuisine(models.Model):
# 	user=models.OneToOneField(User,on_delete=models.CASCADE)
# 	cuisine=models.OneToOneField(MainDish,on_delete=models.CASCADE) password digitalocean illKer_0000_alima

from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)  
    location = models.CharField(max_length=50, default='unknown')
    

    def __str__(self):
        return self.name


class Menu(models.Model):
    DAY_CHOICES = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ]
    day = models.CharField(max_length=3, choices=DAY_CHOICES, default="mon")
    menu = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


    def __str__(self):
        return self.menu


    class Meta:
        unique_together = ('day', 'restaurant')


class User(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    currect_day_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default=1)

    
    def __str__(self):  
        return self.name

    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)








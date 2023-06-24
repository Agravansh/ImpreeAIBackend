from django.db import models

# Create your models here.
class User(models.Model):
    telegram_id = models.IntegerField(primary_key=True)

class Button(models.Model):
    name = models.CharField(max_length=50)

class ButtonCall(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    button = models.ForeignKey(Button, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


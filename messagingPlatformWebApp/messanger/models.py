from django.db import models

# Create your models here.
class Message(models.Model):
    def __str__(self):
        return self.msgText
    msgText = models.CharField(max_length=240)
    msgDate = models.DateTimeField("date sent")
    userFrom = models.CharField(max_length=5)

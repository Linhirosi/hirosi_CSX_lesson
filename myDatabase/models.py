from django.db import models
from django.conf import settings
# Create your models here.

class commentBox(models.Model): #create a SQL sheet
    talker = models.CharField(max_length=20, blank=False)
    comment = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.talker+""+self.comment

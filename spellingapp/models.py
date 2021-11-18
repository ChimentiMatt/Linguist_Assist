from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from datetime import datetime, date

class KeyVal(models.Model):
    spelling_error = models.CharField(max_length=240, db_index=True, default=".", null=True),
    word = models.CharField(max_length=240, db_index=True, default=".", null=True)

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='KeyVals', null=True)
    
    def __str__(self):
        return self.word   




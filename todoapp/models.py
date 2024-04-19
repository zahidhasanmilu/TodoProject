from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class todo(models.Model):
    user = models.ForeignKey(
        User, related_name='user_todo', on_delete=models.CASCADE)
    tode_description = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tode_description
    

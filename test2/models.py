from django.db import models
from django.utils import timezone

# Create your models here.

class Register_User(models.Model):
    name     = models.CharField(max_length=50)
    mobile   = models.CharField(max_length=50,default='Nothing')
    email    = models.CharField(max_length=50) 
    password = models.CharField(max_length=50,)
    selected_type= models.CharField(max_length=50,default='Nothing')
    role    = models.CharField(max_length=50)
    is_active = models.CharField(max_length=50,default='Nothing')
    
    class Meta:
        db_table = 'Register'

    def __int__(self):
        return self.id

class Activities(models.Model):
    activity     = models.CharField(max_length=50)
    participants   = models.CharField(max_length=50)
    sel_type = models.CharField(max_length=50)
    price= models.CharField(max_length=50)
    accessibility    = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    created_date=   models.DateField(default=timezone.now)
    created_by    = models.CharField(max_length=50) 

    
    class Meta:
        db_table = 'activities'

    def __int__(self):
        return self.id



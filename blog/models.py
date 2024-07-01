from django.db import models

# Create your models here.
class Courses(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    duration=models.DurationField()
    
    
    
class Teachers(models.Model):
    full_name=models.CharField(max_length=100)
    status=models.CharField(max_length=50)
    experience=models.IntegerField()
    courses=models.ForeignKey(Courses, on_delete=models.CASCADE)
    
    
    
class Students(models.Model):
    full_name=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    parents_phone_num=models.IntegerField()
    telegram_link=models.CharField(max_length=20)
    address=models.CharField(max_length=12)
    courses=models.ForeignKey(Courses, on_delete=models.CASCADE)
    teachers=models.ForeignKey(Teachers, on_delete=models.CASCADE)
    
    
            
    
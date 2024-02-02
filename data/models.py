from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=30,null=False,blank=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=6, null=False, blank=False)
    dob = models.DateField()
    company = models.CharField(max_length=25, null=False, blank=False)
    department = models.CharField(max_length=25, null=False, blank=False)
    skills = models.CharField(max_length=100, null=False, blank=False)
    salary = models.IntegerField()
    address = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


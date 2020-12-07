from django.db import models
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    email_id    =models.CharField(max_length=120)
    password    =models.CharField(max_length=120)
    uid         =models.CharField(max_length=10)
    name        =models.CharField(max_length=30)
    interests   =models.TextField()
    grade       =models.DecimalField(max_digits=2,decimal_places=1,default=5.0)
    projects    =models.TextField(blank=True,null=True)
    points      =models.DecimalField(max_digits=4,decimal_places=1,default=0.0)

    def get_absolute_url(self):
        #return reverse("all_products",kwargs={"id":self.id})
        return f"/students/self.id/"

    def __str__(self):
        return f'{self.name} : {self.uid}'

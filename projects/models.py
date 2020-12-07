from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=70)
    keywords=models.CharField(max_length=300)
    code=models.TextField(null=True,blank=True)
    author=models.CharField(max_length=30)
    file=models.FileField()

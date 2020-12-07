from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=120)
    ques = models.TextField()


class Stud_Ans(models.Model):
    answer = models.CharField(max_length=400)
    q_id = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    total_upvotes = models.DecimalField(max_digits=4, decimal_places=0, default=0)
    upvote = models.BooleanField(null=True)

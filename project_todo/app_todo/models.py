from django.db import models

# Create your models here.

class taskModel(models.Model):
    title= models.CharField(max_length=100, null=False, blank=False)
    desc = models.TextField(null=False,blank=False)
    due_date=models.DateField(null=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


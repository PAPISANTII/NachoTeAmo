from django.db import models

# Create your models here.
class ErrorReport(models.Model):
    code = models.IntegerField()
    description = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return f"{self.code} - {self.date}"

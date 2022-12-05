from django.db import models

# Create your models here.
class transcript(models.Model):
    url = models.URLField(max_length=255)
    tittle = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
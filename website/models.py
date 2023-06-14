from django.db import models
from phone_field import PhoneField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email=models.EmailField()
    phone = models.CharField(null=True, blank=True, max_length=31)
    subject = models.CharField(max_length=255, null=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering=('-created_date',)


    def __str__(self):
        return self.subject
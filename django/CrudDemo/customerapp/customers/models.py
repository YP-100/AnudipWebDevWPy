from django.db import models

class Customer(models.Model):
    class Meta:
        app_label = 'customerapp'
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add other fields as necessary
    
    def __str__(self):
        return self.name

from django.db import models

class Cellphone (models.Model):
    brand = models.CharField(max_length=20)
    model =  models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="products", null=True)
    
 
    def __str__(self):
        return f"{self.brand} - {self.model} - {self.description}"
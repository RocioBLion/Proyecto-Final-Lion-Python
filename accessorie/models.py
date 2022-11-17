from django.db import models

class Accessorie (models.Model):
    brand = models.CharField(max_length=20)
    model =  models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    price = models.IntegerField()
    image = models.ImageField(upload_to="products", null=True)



    def __str__(self):
        return f"{self.brand} - {self.model} - {self.description} - {self.price}"
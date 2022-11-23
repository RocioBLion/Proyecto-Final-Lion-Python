from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField



class Computer(models.Model):
    brand= models.CharField(max_length=40, null=False, blank=False)
    model = models.IntegerField(null=False, blank=False)
    description = RichTextField(null=True, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='computer', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            "brand",
            "model",
        )
        ordering = ["-created_at"]

    def __str__(self):
        return f"Computer: {self.brand} - {self.model} - {self.description} - {self.price}"


class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Computer (models.Model):
    brand = models.CharField(max_length=20)
    model =  models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='computer', null=True, blank=True)

    def __str__(self):
        return f"{self.brand} - {self.model} - {self.description} - {self.price}"
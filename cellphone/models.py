from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField



class Cellphone(models.Model):
    brand= models.CharField(max_length=40, null=False, blank=False)
    model = models.CharField(max_length=40, null=False, blank=False)
    description = RichTextField(null=True, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cellphone', null=True, blank=True)
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
            "description",
            "price",
        )
        ordering = ["-created_at"]

    def __str__(self):
        return f"Cellphone: {self.brand} - {self.model} - {self.description} - {self.price}"
    
class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "The comment must be longer than 10 characters")
        ]
    )
    cellphone = models.ForeignKey(Cellphone, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

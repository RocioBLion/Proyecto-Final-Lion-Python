from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField



class Computer(models.Model):
    id = models.AutoField(primary_key=True)
    brand= models.CharField(max_length=40, null=False, blank=False)
    model = models.CharField(max_length=40, null=False, blank=False)
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
        ordering = ["id"]

    def __str__(self):
        return f"Computer: {self.brand} - {self.model}"


class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "The comment must be longer than 10 characters")
        ]
    )
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



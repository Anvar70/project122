from django.db import models


# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=False,default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
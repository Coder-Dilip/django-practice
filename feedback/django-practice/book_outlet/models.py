from django.db import models
from  django.core.validators import MinValueValidator,MaxValueValidator


# Create your models here.

class Address(models.Model):
    street=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=5)
    city=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city} {self.street}"


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.first_name} {self.address.city}"


class Book(models.Model):
    title= models.CharField(max_length=50)
    rating= models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author =models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="books")
    is_bestselling_book=models.BooleanField(default=False)
    slug=models.SlugField(default="",blank=True, null=False,db_index=True) #db_index is just for performance
    def __str__(self):
        return f"{self.title} ({self.rating})"




    
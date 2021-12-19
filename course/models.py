from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True,null=False)
    image = models.ImageField(upload_to= 'user/%Y/%m', default= None)
    def __str__(self) -> str:
        return self.name

class ItemBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(max_length=255, null=False)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.subject

class Course(ItemBase):
    class Meta:
        unique_together = ('subject', 'category')

    description = models.TextField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    image = ImageField(upload_to='course/%Y/%m', default= None)
    

class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'course')
    content = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

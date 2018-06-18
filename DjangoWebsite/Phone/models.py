from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    pubDate = models.DateField()
    
    def __str__(self):
        return self.name


class iPhone(models.Model):
    name = models.CharField(max_length=200)
    iphone_id = models.CharField(max_length=200)
    imodel = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def getCategory(self):
        return self.category


class Sony(models.Model):
    name = models.CharField(max_length=200)
    sony_id = models.CharField(max_length=200)
    sony_model = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

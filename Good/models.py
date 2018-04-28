from django.db import models

class Category(models.Model):
  
  class Meta:
    verbose_name = "Категория"
    verbose_name_plural = "Категории"
  
  name = models.CharField(max_length=40)
  
  def __str__(self):
    return self.name

class Good(models.Model):
  
  class Meta:
    verbose_name = "Товар"
    verbose_name_plural = "Товары"
  
  name = models.CharField(max_length=40)
  price = models.IntegerField()
  category = models.ForeignKey(Category, on_delete='CASCADE')
  
  def __str__(self):
    return self.name
  
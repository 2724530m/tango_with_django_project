from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name

    class Meta:
     verbose_name_plural = 'Categories'

     def __str__(self):
      return self.name
  
     def __str__(self):
      return self.name

class Page(models.Model):

 TITLE_MAX_LENGTH = 128 #on page 129 from the link provided i implemented the soloution from the authors git repositry
 URL_MAX_LENGTH = 200 #on page 129 from the link provided i implemented the soloution from the authors git repositry

 title = models.CharField(max_length=TITLE_MAX_LENGTH) #on page 129 from the link provided i implemented the soloution from the authors git repositry
 category = models.ForeignKey(Category, on_delete=models.CASCADE)
 url = models.URLField()
 views = models.IntegerField(default=0)
 likes = models.IntegerField(default=0)


 def __str__(self):
  return self.title
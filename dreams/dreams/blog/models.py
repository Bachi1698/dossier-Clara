from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.nom

class Tag(models.Model):
    nom = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tag' 
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nom

class Article(models.Model):
    image = models.ImageField(upload_to='images/articles')
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name="article_categorie")
    tag = models.ManyToManyField(Tag,related_name="tag_articles")
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = '_'.join((slugify(self.titre),slugify(datetime_now(.microsecond))))
        super(Article,self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="commentaires_user")
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="commentaires_articles")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'commentaire'
        verbose_name_plural = 'commentaires'

    def __str__(self):
        return self.user.username
from django.db import models

# Create your models here.
class About(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/about')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Présentation'
        verbose_name_plural = 'Présentations'

    def __str__(self):
        return self.nom

class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return self.name

class SiteInfo(models.Model):
    mapping = models.URLField(null=True)
    logo = models.ImageField(upload_to='images/site')
    telephone = models.IntegerField()
    email = models.EmailField()
    slogan = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Site info"
        verbose_name_plural = "Sites infos"

    def __str__(self):
        return self.email

class SocialCount(models.Model):
    ICONE = [
        ('facebook','fa-facebook-f'),
        ('twitter','fa-twitte'),
        ('globe','fa-globe'),
        ('behance','fa-behance')
    ]
    reseau = models.CharField(max_length=255)
    lien = models.URLField()
    icones = models.CharField(choices=ICONE,max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "réseau social"
        verbose_name_plural = "réseaux sociaux"

    def __str__(self):
        return self.reseau

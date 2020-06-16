from django.db import models

# Create your models here.
class Project(models.Model):
    TYPE =[
        ('interior','interior'),
        ('exterior','exterior'),
        ('landing','landing'),
    ]
    image = models.ImageField(upload_to="images/project")
    types = models.CharField(choices=TYPE, max_length=255)
    titre = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Poject'
        verbose_name_plural = 'Pojects'

    def __str__(self):
        return self.titre
 
class Appartement(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='images/appartement')
    lieu = models.CharField(max_length=255)
    nombre_douche = models.IntegerField()
    garage = models.BooleanField(default=False)
    superficie = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'appartement'
        verbose_name_plural = 'appartements'

    def __str__(self):
        return self.lieu

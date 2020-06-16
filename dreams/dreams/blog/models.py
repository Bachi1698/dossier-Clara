from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='image/blog')
    description = models.TextField()
    titre = models.CharField(max_length=255)
    commentaire = models.ForeignKey('dreamsApp.Appartement',on_delete=models.CASCADE,related_name='commentaires_blog')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    def __str__(self):
        return self.titre


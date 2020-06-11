from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):

    # Appel de user
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # 1 user <---> 1 profil
    
    # Champs suplementaires
    
    contacts = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='profile/')
    birth_date = models.DateField(null=True)
    genre = models.CharField(max_length=255)

    # Initialisation a la creation
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        
        instance.profile.save()
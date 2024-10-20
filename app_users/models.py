from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .managers import MyUsermanager as UserManager

#verbose_name boshida tursa tenglab otirish shart emas
class User(AbstractUser):
    first_name = models.CharField('First name',max_length=100)
    last_name = models.CharField('Last name',max_length=100)
    username = models.CharField('Username',  max_length=100, null=True, unique=True)
    email = models.EmailField('Email', max_length=100, unique=True)
    bio = models.TextField('About', null=True, blank=True)
    profile_image = models.ImageField('Profile Image', default='profile-images/user-default.png',
                                      null=True, blank=True,
                                      upload_to='profile-images/')

    location = models.CharField('Location', max_length=200, null=True, blank=True)
    occupation = models.CharField('Occupation', max_length=100, null=True, blank=True)
    social_telegram = models.URLField('Telegram Link', null=True, blank=True, max_length=200)
    social_facebook = models.URLField('Facebook Link', null=True, blank=True, max_length=200)
    social_twitter = models.URLField('Twitter Link', null=True, blank=True, max_length=200)
    social_youtube = models.URLField('Youtube Link', null=True, blank=True, max_length=200)
    social_instagram = models.URLField('Instagram Link', null=True, blank=True, max_length=200)
    social_linkedin = models.URLField('Linkedin Link', null=True, blank=True, max_length=200)
    social_whatsapp = models.URLField('WhatsApp Link', null=True, blank=True, max_length=200)
    social_github = models.URLField('GitHub Link', null=True, blank=True, max_length=200)
    social_website = models.URLField('Website Link', null=True, blank=True, max_length=200)

    objects = UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name'
    ]
    def __str__(self):
        return self.email

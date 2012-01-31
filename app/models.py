# Define a custom User class to work with django-social-auth
from django.db import models
from django_dropbox.storage import DropboxStorage

STORAGE = DropboxStorage()

class Image(models.Model):
    photo = models.ImageField(upload_to='photos', storage=STORAGE)

class CustomUserManager(models.Manager):
    def create_user(self, username, email):
        return self.model._default_manager.create(username=username)


class CustomUser(models.Model):
    username = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    def is_authenticated(self):
        return True


from social_auth.signals import pre_update
